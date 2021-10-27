from flask import render_template, jsonify, request
from . import app

@app.route("/")
@app.route("/home.html/")
def home():
    return render_template("home.html")


@app.route("/ajax", methods=["POST"])
def ajax():
    user_text= request.form["userText"]
    print(user_text)
    return jsonify(["pas de réponse"])
