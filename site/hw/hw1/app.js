// Purpose: Google sign-in with Firebase, then send the ID token to a backend.
// Expects HTML elements:
// - #submitBtn: button to start the sign-in flow
// - #log: pre/textarea/div to append status output


// Firebase Web SDK (ES modules over CDN).
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.4/firebase-app.js";
import { getAuth, GoogleAuthProvider, signInWithPopup } from "https://www.gstatic.com/firebasejs/10.12.4/firebase-auth.js";

const firebaseConfig = {
  // Firebase Web API keys are intentionally public and restricted by referrer.
  // See: https://firebase.google.com/docs/projects/api-keys
  // GitHub incorrectly flags the Firebase API key as a secret.

  apiKey: "AIzaSyDTfaBrAa-CbXJNRwlxltVnKVfRvxxyfMQ",
  authDomain: "instant-voyager-485007-v4.firebaseapp.com",
  projectId: "instant-voyager-485007-v4",
  appId: "1:90197506094:web:3f2c95b8276219f574c7bf",
};

// Initialize Firebase app + auth provider.
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

// UI elements.
const logEl = document.getElementById("log");
const submitBtn = document.getElementById("submitBtn");

// Append log lines to the UI.
function log(msg) {
  logEl.textContent += msg + "\n";
}

submitBtn.addEventListener("click", async () => {
  try {
    // 1) Sign in with Google using a popup.
    log("Signing in...");
    const result = await signInWithPopup(auth, provider);
    const user = result.user;

    log(`Signed in as: ${user.email}`);

    // 2) Retrieve a Firebase ID token (JWT) for the signed-in user.
    const idToken = await user.getIdToken();
    log("Got Firebase ID token (JWT). Next: send to backend.");

    // 3) Call backend with the token so it can verify identity.
    const backendUrl = "https://classroom-hw-backend-90197506094.us-central1.run.app";

    const resp = await fetch(`${backendUrl}/whoami`, {
      method: "POST",
      headers: { "Authorization": `Bearer ${idToken}` }
    });

    // 4) Log the backend response (expected to include identity info).
    const data = await resp.json();
    log("Backend /whoami response:\n" + JSON.stringify(data, null, 2));

  } catch (e) {
    // Surface any errors (sign-in or network) to the UI.
    log("Error: " + (e?.message || e));
  }
});
