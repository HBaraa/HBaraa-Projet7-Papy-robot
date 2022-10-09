from flask import render_template, jsonify, request
from . import app

from app_folder.papy_robot.treat_response import ParseResponse


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/ajax", methods=["POST"])
def ajax():
    info = request.data.decode()
    pr = ParseResponse(info)
    dict_returned = pr.parse_resp()
    return jsonify(dict_returned)
