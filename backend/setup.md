### Steps to globally install gcloud and deploy Cloud Run backend(wsl):
Install: curl -sSL https://sdk.cloud.google.com | bash
Accept the defaults
Restart the terminal
Confirm install: gcloud --version
Authenticate: gcloud auth login
If browser doesn't open click the link
Login to Google Cloud SDK (one-time)
Get project id: gcloud projects list
Set Project: gcloud config set project (project id)
Set default region (optional): gcloud config set run/region us-central1
Deploy the backend: 
gcloud run deploy classroom-hw-backend \
  --source backend \
  --allow-unauthenticated \
  --region us-central1
Accept the defaults
This command builds Docker image and deploys the container to Cloud Run.
It creates and returns Service URL such as https://classroom-hw-backend-90197506094.us-central1.run.app
