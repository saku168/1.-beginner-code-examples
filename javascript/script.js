const button = document.querySelector("#change-message");
const message = document.querySelector("#message");

button.addEventListener("click", () => {
  message.textContent = "Nice work — you just used a JavaScript event listener!";
});
