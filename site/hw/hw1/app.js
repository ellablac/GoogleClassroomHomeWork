const logEl = document.getElementById("log");
const submitBtn = document.getElementById("submitBtn");

function log(msg) {
  logEl.textContent += msg + "\n";
}

submitBtn.addEventListener("click", async () => {
  log("Submit clicked (stub). Next step: add Google login + backend call.");
});
