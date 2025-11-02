# scraper/config.py

BASE_URL = "https://issues.apache.org/jira/rest/api/2/search"
PROJECTS = ["KAFKA", "SPARK", "HADOOP"]  
MAX_RESULTS_PER_PAGE = 50
MAX_RETRIES = 3
RATE_LIMIT_WAIT = 3
RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"