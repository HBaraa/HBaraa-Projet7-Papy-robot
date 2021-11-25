function create_element(name, text) {
    var element = document.createElement(name);
    var element_text = document.createTextNode(text);
    element.appendChild(element_text);
    return element;
}

function create_response_div(grandpa_resp) {
    var chat_entry = document.createElement("div")
    chat_entry.setAttribute('class', 'chat');
    var chat_avatar = document.createElement("div")
    chat_avatar.setAttribute('class', 'chat-avatar');
    var you = document.createElement("a");
    you.setAttribute('class', 'avatar avatar-online');
    you.setAttribute('data-toggle', 'tooltip');
    you.setAttribute('href', '#');
    you.setAttribute('data-placement', 'left');
    you.setAttribute('title', '');
    var img = document.createElement("img")
    img.setAttribute('src', '../static/images/papy.png');
    img.setAttribute('alt', 'papyimage');
    img.setAttribute('style', 'position:absolute; left:0px; width:40px; height:40px');
    you.appendChild(img)
    chat_avatar.appendChild(you)
    chat_entry.appendChild(chat_avatar)
    var chat_body = document.createElement("div")
    chat_body.setAttribute('class', 'chat-body');
    chat_body.setAttribute('style', '"background-color: rgb(221, 192, 215);');
    var chat_content = document.createElement("div")
    var grandpy = create_element("p", grandpa_resp)
    chat_content.appendChild(grandpy)
    chat_body.appendChild(chat_content)
    chat_entry.appendChild(chat_body)
    return chat_entry
}

function create_question_div(question) {
    var chat_entry = document.createElement("div")
    chat_entry.setAttribute('class', 'chat');
    var chat_avatar = document.createElement("div")
    chat_avatar.setAttribute('class', 'chat-avatar');
    var you = document.createElement("a");
    you.setAttribute('class', 'avatar avatar-online');
    you.setAttribute('data-toggle', 'tooltip');
    you.setAttribute('href', '#');
    you.setAttribute('data-placement', 'left');
    you.setAttribute('title', '');
    var img = document.createElement("img")
    img.setAttribute('src', '../static/images/user_pic.png');
    img.setAttribute('alt', 'papyimage');
    img.setAttribute('style', 'position:absolute; right:0px; width:40px; height:40px');
    you.appendChild(img)
    chat_avatar.appendChild(you)
    chat_entry.appendChild(chat_avatar)
    var chat_body = document.createElement("div")
    chat_body.setAttribute('class', 'chat-body');
    var chat_content = document.createElement("div")
    chat_content.setAttribute('class', 'chat-content');
    var grandpy = create_element("p", question)
    chat_content.appendChild(grandpy)
    chat_body.appendChild(chat_content)
    chat_entry.appendChild(chat_body)
    return chat_entry
}

let form = document.querySelector("#user-text-form");
let description = document.querySelector("#description");
let accueil = document.querySelector("#home");
let show_info = document.querySelector("#grandpa");
let load_pic = document.querySelector("#load");
show_info.style.visibility = "hidden";
let showtext = "";
let papiresp = "";
function postFormData(url, data) {
    return fetch(url, {
        method: "POST",
        body: document.querySelector("#question").value,
        headers: {
            "Content-type": "plain/text"
        }
    })
        .then(response => response.json())
        .catch(error => console.error());
}
form.addEventListener("submit", function (event) {
    event.preventDefault();
    postFormData("/ajax", new FormData(form))
        .then(response => {
            console.log(response);
            if (response == "") {
                showtext = "Bonjour mon petit, j'ai pas compris ce que tu m'as dit.Dis à papi clairement tu cherche quel endroit";
                papiresp = "Ok papi, je reformulerais ma demande";
                console.log(showtext);
                linkref = "http://127.0.0.1:5000/"
                show_info.style.visibility = "hidden";
            } else {
                paragraph = "";
                for (var i = 0; i < response.length; i++) {
                    let word = response[i];
                    paragraph += word;
                    paragraph += " "
                }
                showtext = "Papi a compris que tu cherche " + paragraph + ". Attends mon poussin papi va te trouver cet endroit ";
                let key_words = paragraph;
                papiresp = "Ok papi";
                linkref = "#grandpa";
            }
            var question = $('#question').val();
            var papyresponse = showtext;
            var chat_box = document.getElementById('chat-box');
            question_entry = create_question_div(question);
            question_entry.style.background = "rgb(243, 188, 231)";
            question_entry.style.color = "blue";
            question_entry.style.fontsize = "x-large";
            chat_box.appendChild(question_entry);
            let newtext = create_response_div(papyresponse);
            chat_box.append(newtext);
            newtext.style.color = "magenta";
            newtext.style.background = "rgb(152, 205, 240)";
            var btn = document.createElement("button");
            var t = document.createTextNode(papiresp);    // Créer un noeud textuel
            btn.appendChild(t);   // Ajouter le texte au bouton
            chat_box.appendChild(btn);
            btn.style.background = "rgb(243, 188, 231)";
            btn.addEventListener("click", function (event) {
                event.preventDefault();
                setTimeout(() => {
                    load_pic.style.visibility = "visible";
                }, 5000);
                newtext.remove();
                btn.remove();
                location.href = linkref;
                accueil.style.visibility = "hidden";
                if (response == "") {
                    pass;
                } else {
                    setTimeout(() => {
                        load_pic.style.visibility = "visible";
                    }, 500);
                    setTimeout(() => {
                        load_pic.style.visibility = "hidden";
                        show_info.style.visibility = "visible";
                    }, 5000);
                }
            });
        })
});
let startpresent = document.querySelector("#startpresent");
let present = document.querySelector("#presentation");
startpresent.addEventListener("click", function (event) {
    event.preventDefault();
    accueil.style.visibility = "hidden";
    present.style.visibility = "visible";
})
