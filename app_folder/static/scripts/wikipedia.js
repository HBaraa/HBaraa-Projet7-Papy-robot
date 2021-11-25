var random_answer_google = ['Bien sûr mon kiki! Voici l\'adresse : ', 'Hum... si je ne dis pas de bétise ça se trouve ici :']
var random_answer_wiki = ['C\'est marrant que tu me demandes ça, je vais te raconter ! ', 'Maintenant que t\'en parles, ça me fait penser.']


function get_random_answer(answer_type) {
    var random_number = Math.floor(Math.random() * (3 - 1)) + 0;
    if (answer_type == "google") {
        var answer = random_answer_google[random_number];
    } else {
        var answer = random_answer_wiki[random_number];
    }

    return answer;
}

function create_element(name, text) {
    var element = document.createElement(name);
    var element_text = document.createTextNode(text);
    element.appendChild(element_text);
    return element;
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

    chat_avatar.appendChild(you)
    chat_entry.appendChild(chat_avatar)

    var chat_body = document.createElement("div")
    chat_body.setAttribute('class', 'chat-body');

    var chat_content = document.createElement("div")
    chat_content.setAttribute('class', 'chat-content');
    // Create p
    var grandpy = create_element("p", question)

    chat_content.appendChild(grandpy)
    chat_body.appendChild(chat_content)
    chat_entry.appendChild(chat_body)

    return chat_entry
}

function create_positive_answer_wiki_div(answer, url_div, wiki_summary) {
    // Create div class="chat"
    var chat_entry = document.createElement("div")
    chat_entry.setAttribute('class', 'chat  chat-left');

    var chat_avatar = document.createElement("div")
    chat_avatar.setAttribute('class', 'chat-avatar');

    var you = document.createElement("a");
    you.setAttribute('class', 'avatar avatar-online');
    you.setAttribute('data-toggle', 'tooltip');
    you.setAttribute('href', '#');
    you.setAttribute('data-placement', 'left');
    you.setAttribute('title', '');

    chat_avatar.appendChild(you)
    chat_entry.appendChild(chat_avatar)

    var chat_body = document.createElement("div")
    chat_body.setAttribute('class', 'chat-body');

    var chat_content = document.createElement("div")
    chat_content.setAttribute('class', 'chat-content');

    var grandpy = create_element("p", answer)

    var summary = create_element("p", wiki_summary)
    summary.appendChild(url_div)
    grandpy.appendChild(summary)

    chat_content.appendChild(grandpy)

    chat_body.appendChild(chat_content)
    chat_entry.appendChild(chat_body)


    return chat_entry
}

$(document).ready(function () {

    $('#demand').click(function (e) {
        e.preventDefault();
        var question = $('#question').val();


        // Sentence Div Creation
        var chat_box = document.getElementById('chat-box');

        question_entry = create_question_div(question)
        chat_box.appendChild(question_entry)
        var responce = document.getElementById('chat-box');
        resp_output = get_random_answer()
        resp_output.appendChild(responce)
        $.ajax({
            url: "/demand",
            type: "POST",
            data: question,
            dataType: "text",

            success: function (response, textStatus, jqXHR) {
                var obj = JSON.parse(response);

                var url = document.createElement("a");
                var url_text = document.createTextNode(" Si tu veux en savoir plus, c'est par ici!")
                url.setAttribute('href', obj.info.url);
                url.setAttribute('target', '_blank');
                url.appendChild(url_text);
                wiki_answer_entry = create_positive_answer_wiki_div(get_random_answer("wiki"), url, obj.info.summary)

                chat_box.appendChild(wiki_answer_entry)

            },
        });

    });
});
