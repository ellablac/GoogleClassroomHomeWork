import argparse
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/classroom.courses.readonly"]

ap = argparse.ArgumentParser()
ap.add_argument("--course_id", required=True, help="Google Classroom courseId")
flow = InstalledAppFlow.from_client_secrets_file("scripts/oauth_client.json", SCOPES)
creds = flow.run_local_server(port=0)

svc = build("classroom", "v1", credentials=creds, cache_discovery=False)
resp = svc.courses().courseWork().list(courseId=ap.parse_args().course_id, pageSize=50).execute()

for c in resp.get("courseWork", []):
    print(c["id"], "-", c.get("title"))
    print(c)