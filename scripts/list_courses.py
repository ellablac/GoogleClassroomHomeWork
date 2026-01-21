from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/classroom.courses.readonly"]

flow = InstalledAppFlow.from_client_secrets_file("scripts/oauth_client.json", SCOPES)
# creds = flow.run_local_server(port=0)
creds = flow.run_local_server(port=0, open_browser=False)

svc = build("classroom", "v1", credentials=creds, cache_discovery=False)
resp = svc.courses().list(pageSize=50).execute()

for c in resp.get("courses", []):
    print(c["id"], "-", c.get("name"))
    print(c)