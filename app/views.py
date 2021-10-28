from flask import render_template, jsonify
from . import app

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/ajax", methods=["POST"])
def ajax():
    return jsonify(["pas de réponse"])
