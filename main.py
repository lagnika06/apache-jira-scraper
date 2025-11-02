from scraper.jira_scraper import JiraScraper
from scraper.data_transformer import transform_to_jsonl
from scraper.config import PROJECTS

def main():
    scraper = JiraScraper()
    scraper.scrape_all_projects()
    for project in PROJECTS:
        transform_to_jsonl(project)

if __name__ == "__main__":
    main()