document.addEventListener('DOMContentLoaded', function (event){
    let form = document.querySelector(".login-form");
    console.log(form)
    form.addEventListener("submit", event =>{
        event.preventDefault();
        const formData = new FormData(event.target);
        const data = {
            email: formData.get("email"),
            password: formData.get("password")
        };

        const url = event.target.action;

        fetch(url, {
            method: "post",
            headers: {
                'Content-Type' : 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            return response.json();
        })
        .then (data => {
            console.log("success", data);
            const response_element = document.getElementById("login-json");
            console.log(response_element);
            DisplayJson(data, response_element);
        })
        .catch(error => {
            alert(error);
            console.log(error);
        });
    });
});
