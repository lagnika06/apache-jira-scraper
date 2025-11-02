import json
import os
from scraper.config import RAW_DATA_PATH, PROCESSED_DATA_PATH

def transform_to_jsonl(project):
    input_file = os.path.join(RAW_DATA_PATH, f"{project}_issues.json")
    output_file = os.path.join(PROCESSED_DATA_PATH, f"{project}_issues.jsonl")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(input_file, "r", encoding="utf-8") as f_in, \
         open(output_file, "w", encoding="utf-8") as f_out:

        issues = json.load(f_in)
        for issue in issues:
            data = {
                "id": issue["id"],
                "title": issue["fields"]["summary"],
                "status": issue["fields"]["status"]["name"],
                "description": issue["fields"].get("description", ""),
                "comments": [c["body"] for c in issue["fields"].get("comment", {}).get("comments", [])],
                "project": issue["fields"]["project"]["key"],
                "reporter": issue["fields"]["reporter"]["displayName"] if issue["fields"].get("reporter") else None,
                "created": issue["fields"]["created"],
                "updated": issue["fields"]["updated"],
                "derived_tasks": [
                    {"task_type": "summarization", "instruction": "Summarize the issue."},
                    {"task_type": "qna", "instruction": "Generate QnA pairs from the description and comments."}
                ]
            }
            f_out.write(json.dumps(data) + "\n")

    print(f"✅ Transformed data for {project} saved at {output_file}")