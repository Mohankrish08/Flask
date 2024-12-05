document.addEventListener("DOMContentLoaded", function () {
    const usernameInput = document.getElementById("username");
    const passwordInput = document.getElementById("password");
    const submitBtn = document.getElementById("submitBtn");

    submitBtn.addEventListener("click", function(e) {
        e.preventDefault();

        const username = usernameInput.value.trim();
        const password = passwordInput.value.trim();

        let isValid = true;
        let errorMessage = "";

        usernameInput.classList.remove("error");
        passwordInput.classList.remove("error");

        if (!username) {
            usernameInput.classList.add("error");
            isValid = false;
        }

        if (!password) {
            errorMessage = "Password cannot be empty.";
            passwordInput.classList.add("error");
            isValid = false;
          } else if (password.length < 8) {
            errorMessage = "Password needs to be more than 8 characters long!";
            passwordInput.classList.add("error");
            isValid = false;
          }


        if (!isValid) {
            alert(errorMessage)
        };

        if (isValid) {
            const data = {
                username: username,
                password: password
            }
        

        
        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            console.log("Server Response:", data); 
            if (data.code === 400) {
                alert(data.message); 
            } else if (data.code === 200) {
                alert(data.message); 
            }
        })
        .catch(error => {
            console.error('Fetch Error:', error);
            alert('An error occurred during login');
        });
        };
    })
    
    
})

