let member_num = 0;

document.addEventListener("DOMContentLoaded", function(event){
    const button = document.getElementById("add-member");
    button.addEventListener("click", function(event){
        event.preventDefault();
        member_num++;
        console.log(`button : ${event.target}, ${member_num}`);
        const div = document.createElement('div');
        div.setAttribute("id", `member-${member_num}`)
        div.className = 'form-input'

        const name_label = document.createElement("label");
        name_label.textContent = "Name";
        name_label.setAttribute("for", `name-${member_num}`);

        const name_input = document.createElement("input");
        name_input.setAttribute("name", `member-name-${member_num}`);
        name_input.setAttribute("id", `name-${member_num}`);
        name_input.setAttribute("type", "text");

        div.appendChild(name_label);
        div.appendChild(name_input);

        const email_label = document.createElement("label");
        email_label.textContent = "Email"
        email_label.setAttribute("for", `email-${member_num}`);

        const email_input = document.createElement("input");
        email_input.setAttribute("name", `member-email-${member_num}`);
        email_input.setAttribute("id", `email-${member_num}`);
        email_input.setAttribute("type", "email");

        div.appendChild(email_label);
        div.appendChild(email_input);

        const access_label = document.createElement("label");
        access_label.textContent = "Access Level"
        access_label.setAttribute("for", `access-${member_num}`);

        const access_input = document.createElement("input");
        access_input.setAttribute("name", `member-access-${member_num}`);
        access_input.setAttribute("id", `access-${member_num}`);
        access_input.setAttribute("type", "text");

        div.appendChild(access_label);
        div.appendChild(access_input);

        const delete_button = document.createElement('button');
        delete_button.textContent = "Delete Member";
        delete_button.addEventListener('click', function(event){
            const element = document.getElementById(`member-${member_num}`);
            element.remove();
            member_num--;
        });

        div.appendChild(delete_button);

        document.querySelector('.organization-form').appendChild(div);
    });
});
