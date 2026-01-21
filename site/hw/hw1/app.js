import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.4/firebase-app.js";
import { getAuth, GoogleAuthProvider, signInWithPopup } from "https://www.gstatic.com/firebasejs/10.12.4/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyDTfaBrAa-CbXJNRwlxltVnKVfRvxxyfMQ",
  authDomain: "instant-voyager-485007-v4.firebaseapp.com",
  projectId: "instant-voyager-485007-v4",
  appId: "1:90197506094:web:3f2c95b8276219f574c7bf",
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

const logEl = document.getElementById("log");
const submitBtn = document.getElementById("submitBtn");

function log(msg) {
  logEl.textContent += msg + "\n";
}

submitBtn.addEventListener("click", async () => {
  try {
    log("Signing in...");
    const result = await signInWithPopup(auth, provider);
    const user = result.user;

    log(`Signed in as: ${user.email}`);

    const idToken = await user.getIdToken();
    log("Got Firebase ID token (JWT). Next: send to backend.");
    // We'll use this in Step 5.2
    // console.log("ID TOKEN:", idToken);
  } catch (e) {
    log("Error: " + (e?.message || e));
  }
});
