const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username && password === "web_dev") {
        alert("You have successfully logged in.");
        window.location.replace("dashboard.html");
    } else {
        alert("Try again, but this time with a better password(web_dev)");
    }
})