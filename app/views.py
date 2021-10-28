from flask import render_template, jsonify, request
from . import app

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/presentation")
def presentation():
    return render_template("presentation.html")


@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["question"]
    print("la requéte est : ", user_text)
    return jsonify(["pas de réponse"])
