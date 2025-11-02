🧠 Apache JIRA Scraper
🚀 Overview

The Apache JIRA Scraper automates the extraction and transformation of issue data from various Apache Software Foundation projects using the JIRA REST API.

It collects raw issue metadata (ID, project, summary, status, timestamps, etc.), cleans and standardizes the data into structured JSONL format, and prepares it for downstream analytics, dashboards, or machine learning pipelines.

This project demonstrates a complete data engineering mini-pipeline — from API ingestion to data transformation and storage — with modular, production-ready code.

🗂️ Project Structure
apache-jira-scraper/
│
├── scraper/
│   ├── config.py            # API configuration and project settings
│   ├── jira_scraper.py      # Fetches issues from Apache JIRA REST API
│   ├── data_transformer.py  # Cleans, normalizes, and saves structured data
│   └── utils.py             # Logging, helper, and utility functions
│
├── data/
│   ├── raw/                 # Stores raw API responses (ignored in .gitignore)
│   └── processed/           # Stores cleaned JSONL outputs (ignored in .gitignore)
│
├── logs/                    # Application logs (ignored in .gitignore)
│
├── main.py                  # Entry point: runs the complete pipeline
├── requirements.txt         # Python dependencies
├── .gitignore               # Ignore rules for large or transient files
└── README.md                # Documentation

⚙️ Installation
# Clone the repository
git clone https://github.com/lagnika06/apache-jira-scraper.git
cd apache-jira-scraper

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate     # On Mac/Linux
venv\Scripts\activate        # On Windows

# Install dependencies
pip install -r requirements.txt

▶️ Usage

Run the entire scraping and transformation pipeline:

python main.py


This will:

Fetch JIRA issues from Apache projects (defined in scraper/config.py)

Save the raw responses in data/raw/

Clean and normalize the data

Store structured output as JSONL files in data/processed/

📁 Example Output

Example record from data/processed/sample.jsonl:

{
  "id": "KAFKA-14873",
  "project": "Kafka",
  "summary": "Fix consumer offset tracking issue",
  "status": "Resolved",
  "created": "2025-10-14T10:45:00Z",
  "updated": "2025-10-17T09:12:00Z",
  "assignee": "JohnDoe"
}

💡 Key Features

✅ Automated Data Scraping – Extracts issue data via JIRA REST API
✅ Config-Driven Design – All project and endpoint settings stored in config.py
✅ Data Transformation – Cleans, normalizes, and outputs structured JSONL
✅ Logging & Error Handling – Tracks each step with retry logic for failures
✅ Modular Codebase – Separate layers for scraping, transforming, and utilities
✅ Version Control Ready – Clean .gitignore, .gitkeep placeholders

🧩 Tech Stack
Category	Tools / Libraries
Language	Python 3.9+
Data Handling	JSON / JSONL
API Client	requests
Logging	logging
Virtual Environment	venv
📊 Workflow Overview
            ┌─────────────────────┐
            │  Apache JIRA API    │
            └─────────┬───────────┘
                      │
                      ▼
        ┌──────────────────────────┐
        │  jira_scraper.py         │  → Fetch raw JSON
        └─────────┬────────────────┘
                  │
                  ▼
        ┌──────────────────────────┐
        │  data_transformer.py     │  → Clean, normalize, convert
        └─────────┬────────────────┘
                  │
                  ▼
        ┌──────────────────────────┐
        │   data/processed/*.jsonl │  → Ready for analytics
        └──────────────────────────┘

⚠️ Data Notes

📌 The raw and processed data folders are excluded from GitHub to avoid large file uploads (>25 MB).
Empty directories are preserved using .gitkeep files and are automatically populated when the scraper runs.

🚀 Future Enhancements

 Integrate with Elasticsearch or BigQuery for scalable storage

 Add Airflow or cron jobs for scheduled scraping

 Include data visualization dashboards (issue trends, resolution times)

 Implement unit tests for scraper and transformer modules

🧑‍💻 Author

Lagnika Dagur
🎓 B.Tech, Computer Science & Engineering
💼 AI | Cloud | Data Engineering Enthusiast
🌐 GitHub: lagnika06


🌟 Acknowledgments

Special thanks to Scaler Academy for the opportunity to implement real-world engineering projects involving data scraping, transformation, and structured pipelines.
