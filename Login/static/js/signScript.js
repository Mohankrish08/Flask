document.addEventListener("DOMContentLoaded", function() {
    const usernameInput = document.getElementById("username");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const confimpassInput = document.getElementById("confirm-password");
    const submitBtn = document.getElementById("sign-up");

    submitBtn.addEventListener("click", function(e) {
        e.preventDefault(); // Prevent form submission

        const username = usernameInput.value.trim();
        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();
        const confirmpass = confimpassInput.value.trim();

        let isValid = true;
        let errorMessage = "";

        usernameInput.classList.remove("error");
        passwordInput.classList.remove("error");
        confimpassInput.classList.remove("error");

        if (!username) {
            errorMessage = "Username cannot be empty.";
            usernameInput.classList.add("error");
            isValid = false;
        }

        if (!password) {
            errorMessage = "Password cannot be empty.";
            passwordInput.classList.add("error");
            isValid = false;
        } else if (password.length < 8) {
            errorMessage = "Password needs to be at least 8 characters long!";
            passwordInput.classList.add("error");
            isValid = false;
        }

        if (password !== confirmpass) {
            errorMessage = "Passwords do not match!";
            confimpassInput.classList.add("error");
            isValid = false;
        }

        if (!isValid) {
            alert(errorMessage);
        } else {
            const data = {
                username: username,
                email: email,
                password: password,
            };

            console.log("Form Data:", data);
            alert("Sign-up successful!");
        }
    });
});
