import json
import os

# Read GitHub event payload
with open(os.environ['GITHUB_EVENT_PATH']) as f:
    event = json.load(f)

payload = event.get("client_payload", {})
summary = payload.get("summary", "No summary provided")
description = payload.get("description", "No description provided")

print(f"Summary: {summary}")
print(f"Description: {description}")
