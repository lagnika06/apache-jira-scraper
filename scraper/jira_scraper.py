import requests
from scraper.config import BASE_URL, PROJECTS, MAX_RESULTS_PER_PAGE, RAW_DATA_PATH
from scraper.utils import retry_request, save_json
import os

class JiraScraper:
    def __init__(self):
        self.session = requests.Session()

    def fetch_issues(self, project_key):
        all_issues = []
        start = 0
        total = 1  # dummy to enter loop

        while start < total:
            params = {
                "jql": f"project={project_key}",
                "startAt": start,
                "maxResults": MAX_RESULTS_PER_PAGE,
            }

            data = retry_request(self.session, BASE_URL, params)
            if not data or "issues" not in data:
                break

            issues = data["issues"]
            total = data.get("total", 0)
            all_issues.extend(issues)
            start += len(issues)

        save_path = os.path.join(RAW_DATA_PATH, f"{project_key}_issues.json")
        save_json(all_issues, save_path)
        return all_issues

    def scrape_all_projects(self):
        for project in PROJECTS:
            print(f"Scraping {project}...")
            self.fetch_issues(project)