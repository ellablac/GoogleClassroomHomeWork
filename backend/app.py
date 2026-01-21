import os
from flask import Flask, request, jsonify

import firebase_admin
from firebase_admin import auth as fb_auth, credentials

app = Flask(__name__)

# Initialize Firebase Admin (for verifying Firebase ID tokens)
if not firebase_admin._apps:
    # For Cloud Run, we’ll provide service account JSON via an env var later.
    # Locally, you can also use GOOGLE_APPLICATION_CREDENTIALS.
    if os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON"):
        cred = credentials.Certificate(os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON"))
    else:
        cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred)

@app.get("/health")
def health():
    return "ok", 200

@app.post("/whoami")
def whoami():
    authz = request.headers.get("Authorization", "")
    if not authz.startswith("Bearer "):
        return jsonify({"error": "Missing Authorization: Bearer <Firebase ID token>"}), 401

    id_token = authz.split(" ", 1)[1].strip()
    try:
        decoded = fb_auth.verify_id_token(id_token)
        # decoded often contains email if Google sign-in, but not guaranteed unless present
        return jsonify({
            "ok": True,
            "uid": decoded.get("uid"),
            "email": decoded.get("email"),
            "claims": {k: decoded.get(k) for k in ["iss", "aud", "sub"]},
        })
    except Exception as e:
        return jsonify({"error": f"Invalid token: {e}"}), 401

"""
Setup (unix):
Install gcloud: curl -sSL https://sdk.cloud.google.com | bash
Restart the terminal
Authenticate:
gcloud auth login
Set Project:
gcloud config set project GoogleClassroomHomeWork
"""