

function DisplayJson(json, element){
    element.textContent = JSON.stringify(json, undefined, 2);
}

function AddToken(name, token){
    const element = document.querySelector(`#${name}`);
    element.setAttribute("value", token);
}

document.addEventListener("DOMContentLoaded", function(event){
    const forms =  document.querySelectorAll("form");
    forms.forEach(form => {
        form.addEventListener("submit", function(event){
            event.preventDefault();
            const form = event.target;
            let formData = new FormData(form);
            let requestObject = {
                method: form.method,
                headers: {
                    'Content-Type' : 'application/json',
                }
            }
            let data = {};
            let members = [];
            formData.forEach((value, key) => {
                if(key != "response-element" && key != "access-token"){
                    if(key.includes('member')){
                       let id = key.split('-')[2];
                       let member = {
                        name: formData.get(`member-name-${id}`),
                        email: formData.get(`member-email-${id}`),
                        access_level: formData.get(`member-access-${id}`)
                       };
                       members.push(member);
                       formData.delete(`member-name-${id}`);
                       formData.delete(`member-email-${id}`);
                       formData.delete(`access-${id}`);
                    }
                    else{
                        data[key] = value;
                    }
                }
                data["members"] = members;
                if(key == "access_token"){
                    requestObject.headers["Authorization"] = `Bearer ${value}`;
                }
                console.log(requestObject);
            });
            console.log(data);
            requestObject.body = JSON.stringify(data);
            fetch(form.action, requestObject).
            then(response => {
                return response.json();
            }).
            then(data =>{
                console.log("success", data);
                const response_element = document.getElementById(formData.get("response-element"));
                DisplayJson(data, response_element);
                console.log(`${"access_token" in data}`);
                if("access_token" in data){
                    AddToken('access-token', data.access_token);
                }
                if ("refresh_token" in data){
                    AddToken('refresh-token', data.refresh_token);
                }
            }).
            catch(error => {
                console.log(error);
            });
        });
    });
});
