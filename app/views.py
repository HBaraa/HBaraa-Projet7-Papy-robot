from flask import render_template, jsonify, request
from werkzeug.wrappers import response
from . import app
from .utils import transform_to_upper

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/presentation", methods= ["GET"])
def presentation():
    return render_template("presentation.html")


@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["question"]
    response = transform_to_upper(user_text)
    return jsonify(response)
