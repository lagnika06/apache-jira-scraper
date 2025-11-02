import time
import json
import logging
import os

logging.basicConfig(
    filename='logs/scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def retry_request(session, url, params, retries=3, wait=3):
    for attempt in range(retries):
        try:
            response = session.get(url, params=params, timeout=10)
            if response.status_code == 429:
                logging.warning("Rate limit hit. Waiting...")
                time.sleep(wait * 2)
            elif response.status_code >= 500:
                logging.warning("Server error, retrying...")
                time.sleep(wait)
            else:
                response.raise_for_status()
                return response.json()
        except Exception as e:
            logging.error(f"Attempt {attempt+1} failed: {e}")
            time.sleep(wait)
    return None

def save_json(data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)