async function refreshMap(latitude, longitude, place) {
    let map;
    let marker;
    let lati = latitude;
    let long = longitude;
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: lati, lng: long },
        zoom: 15,
    });

    marker = new google.maps.Marker({
        position: { lat: lati, lng: long },
        map: map,
    })

    google.maps.event.addListener(marker, "click", function () {
        open(`https://maps.google.com/maps?hl=fr&q=${place}`, Window)
    });
};
let u = document.getElementById('dial_area')

async function display_message(sender_datas, msg) {

    let answer

    if (sender_datas.role == "user") { // to display user msg // Call before fetch
        answer = `<p style="margin: 0;">${msg}<p>`;
        display_it(sender_datas, answer)
    }
    else if (sender_datas.role == "robot") {

        if (msg == 0) { // to display loading icon // call before fetch
            let loading_icon = `<img src='static/images/loading-fast.gif' class="gif">`;
            sender_datas.role = "robot_load"
            display_it(sender_datas, loading_icon)
            sender_datas.role = "robot"
        };

        if (msg.greetings == 1) { // analyse if grandpy need to responde by greetings

            answer = "Bien le bonjour 👋 ! ";
            let r = document.getElementById('robot_load');
            if (r !== null) {
                r.innerHTML = answer; // del loading gif replace greeting msg 
                r.setAttribute("id", "robot");
            }
            else {
                display_it(sender_datas, answer);
            }
            msg.greetings = 0; // pass greetings to 0 

        };

        if (msg.greetings == 0) { // If greetings done or if they are not

            let rb = document.getElementById('robot_load');
            if (rb !== null) {
                rb.parentElement.remove()   // to remove loading gif
            }

            let datas = JSON.parse(JSON.stringify(msg));
            // if there are map_datas -> display adresse && refresh map / add marker
            if (datas.map_data !== null) {   // "null" is to unfound results 
                if (datas.map_data != 0) {  // and "0" if user just say "Hi"

                    answer = `Bien sûr mon poussin ! La voici :</br>
                              </br>
                              ${datas.map_data["place"]}</br>
                              ${datas.map_data["address"]}`;

                    display_it(sender_datas, answer); // display map_data
                    refreshMap(datas.map_data.coordinates["lat"], datas.map_data.coordinates["lng"],
                        datas.map_data["place"]);

                    // if there are map data, and also anecdote
                    if (datas.anecdote !== null) {
                        if (datas.anecdote != 0) {
                            answer = `Mais t'ai-je déjà raconté l'histoire sur de ce quartier qui m'a 
                            vu en culottes courtes ?</br></br> ${datas.anecdote}`;
                            display_it(sender_datas, answer); // display anecdote
                        };
                    };
                };
            }
            else { // if there not found response display error_msg
                answer = datas.anecdote;
                display_it(sender_datas, answer)
            };
        };
    };
};
function display_it(sender_datas, response) {

    let container_html = `
        <div id='${sender_datas.role}_box'>\
            <div id="${sender_datas.role}">\
                ${response}
            </div>\
            <div id='emot_talker'>${sender_datas.icon}</div>\
        </div>
        `;

    u.insertAdjacentHTML("beforeend", container_html);
    u.lastElementChild.scrollIntoView({ behavior: "smooth", block: "end", inline: "end" });
};
// 🏘️🚩👴

let user_data = { role: "user", icon: '🧐' };
let robot_data = { role: "robot", icon: '🤖' };

async function SendRequest(msg) {

    display_message(user_data, msg); //display user message
    display_message(robot_data, 0) // display gif loading

    let msg_json = `{"msg": "${msg}"}`;

    let url = '/grandpy/';
    let mode = "POST";

    fetch(url, { method: mode, body: msg_json })
        .then(response => response.json())
        .then(response => display_message(robot_data, response))
}
let b = document.getElementById('demand');
let t = document.getElementById('question');
let i = document.getElementById("question");
let l = document.getElementById("img_send")

function main() {

    b.addEventListener('click', (e) => {

        let msg = document.input_msg.textarea.value;

        if (msg.length < 2 || msg == " ") {
            i.reset();
        }
        else {
            SendRequest(msg);
        }
        i.reset();
    });

    t.addEventListener('keydown', (e) => {
        if (event.keyCode == 13) {
            b.click();
        }
    });

    t.addEventListener('keyup', (e) => {
        if (event.keyCode == 13) {
            i.reset();
        }
    });

    l.addEventListener('click', (e) => {
        window.open("https://github.com/AlexisFricard/P7_GrandPyBot");
    });

    l.addEventListener("mouseover", (e) => {
        // on met l'accent sur la cible de mouseover
        l.setAttribute("class", "zoom");
    });

    l.addEventListener("mouseout", (e) => {
        // on met l'accent sur la cible de mouseover
        l.setAttribute("class", "logo_box");
    });

}

main();
