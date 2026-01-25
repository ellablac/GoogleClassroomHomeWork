"""
Flask backend for verifying Firebase ID tokens.

Endpoints:
- GET /health: lightweight health check.
- POST /whoami: verifies a Firebase ID token and returns identity info.

Auth:
- Expects an Authorization header: "Bearer <Firebase ID token>".

Environment:
- FIREBASE_SERVICE_ACCOUNT_JSON: optional service account JSON string.
  If not set, Application Default Credentials are used.
"""

import os
from typing import Any

from flask import Flask, request, jsonify, Response

import firebase_admin
from firebase_admin import auth as fb_auth, credentials

app = Flask(__name__)

ALLOWED_ORIGINS = {
    "http://localhost:8000",
    "http://localhost:5500",
    "http://127.0.0.1:8000",
    "https://ellablac.github.io",
}

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
    """Return a basic health check response."""
    return "ok", 200

@app.route("/whoami", methods=["POST", "OPTIONS"])
def whoami():
    """Verify a Firebase ID token and return basic identity claims."""
    if request.method == "OPTIONS":
        return ("", 204)
    
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


@app.after_request
def add_cors_headers(resp):
    """Attach CORS headers for approved origins."""
    origin = request.headers.get("Origin")
    if origin in ALLOWED_ORIGINS:
        resp.headers["Access-Control-Allow-Origin"] = origin
        resp.headers["Vary"] = "Origin"
        resp.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
        resp.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    return resp
