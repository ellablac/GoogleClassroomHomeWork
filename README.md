# Google Classroom HomeWork Integration

## Overview
I need a better way to create homework for my language students. Google Classroom’s assignment tools are limited. For example, it is not possible to create interactive games or easily include graphics. Graded assignments are restricted to true/false, multiple choice, free-text responses.

## Plan:

* Use the Google Classroom API to connect my website with Google Classroom.

* Host homework on my website, where students can submit their work; each submission will trigger a grade update in Google Classroom.

* Use Google Firebase Authentication so students can sign in with their Google accounts.

* Since Google only allows grade updates via the API from the same project that created the assignment, assignments will also need to be created via the API (script-based for now, no UI).

## Implementation Details
### Google Cloud Project
Name: GoogleClassroomHomework 
Project contains:
* Classroom API calls that create the coursework in Google Classroom
* Classroom API calls that submit grade and return homewok
* OAuth client
* Serverless backend deployment (Google Cloud Run)

### Firebase Auth
* Allows students to sign in to my website with their Google credentials. They must use user ids they use in the Google Classroom.

### Configuration steps
- Create Google Cloud project 
- Enable Google Classroom API
- Configure OAuth consent screen (External) and add test users
- Initially up to 100 test users can use the  application. Production use will require additional app verification steps.
- Create Desktop OAuth client and downloaded client credentials (keep out of repo)
