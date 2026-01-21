"""
Create a Google Classroom coursework assignment that links to a homework page.

The script launches a local OAuth flow, creates an ASSIGNMENT in the target
course, and prints the created coursework details.

Example:
python scripts/create_coursework.py --course_id 840528145865 --title "HW1: Test submission" --link "https://ellablac.github.io/GoogleClassroomHomeWork/site/hw/hw1/" --max_points 100 --state DRAFT
"""

import argparse
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/classroom.coursework.students"]

def main():
    """
    Parse CLI args, authenticate, and create a Classroom assignment.
    """

    ap = argparse.ArgumentParser()
    ap.add_argument("--course_id", required=True, help="Google Classroom courseId")
    ap.add_argument("--title", required=True)
    ap.add_argument("--link", required=True, help="Homework page URL (GitHub Pages)")
    ap.add_argument("--max_points", type=int, default=100)
    ap.add_argument("--state", default="DRAFT", choices=["PUBLISHED", "DRAFT"])
    ap.add_argument("--oauth_json", default=str(Path("scripts/oauth_client.json")))
    args = ap.parse_args()

    """
    Run a local OAuth flow (InstalledAppFlow.run_local_server) with scope 
    https://www.googleapis.com/auth/classroom.coursework.students to get credentials.
    """
    flow = InstalledAppFlow.from_client_secrets_file(args.oauth_json, SCOPES)
    creds = flow.run_local_server(port=0)

    """
    Build here is googleapiclient.discovery.build from the Google API Python client. 
    It constructs a service client for Google classrom API v1 using given credentials.
    The returned svc is googleapiclient.discovery.Resource object. 
    That object exposes the Classroom API’s resources and methods.
    """
    svc = build("classroom", "v1", credentials=creds, cache_discovery=False)

    body = {
        "title": args.title,
        "workType": "ASSIGNMENT",
        "state": args.state,
        "maxPoints": args.max_points,
        "materials": [{"link": {"url": args.link}}],
    }
    """
    The 'execute' method makes a POST request to the Classroom API 
    to create coursework in the specified course.
    """
    created = svc.courses().courseWork().create(courseId=args.course_id, body=body).execute()

    print("✅ Created CourseWork")
    print("courseId:", args.course_id)
    print("courseWorkId:", created["id"])
    print("alternateLink:", created.get("alternateLink"))
    print("maxPoints:", created.get("maxPoints"))
    print("state:", created.get("state"))
    if created.get("state") == "DRAFT":
        print("📝 Assignment is in DRAFT state.")
        print("👉 Remember to publish it in Google Classroom to notify students.")

if __name__ == "__main__":
    main()
