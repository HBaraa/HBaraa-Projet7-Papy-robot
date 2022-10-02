from flask import  Flask, render_template, jsonify, request
from . import app

from app_folder.PapyRobot.resp_treatment import TreatResponse, ParseResponse


@app.route("/")
def home():
    infos = ajax()
    # print(type(infos))
    # print(infos)
    # print("******Youpyyyyy=====")
    return render_template("home.html")


@app.route("/ajax", methods=["POST"])
def ajax():
    info = request.data.decode()
    pr = ParseResponse(info)
    dict_returned = pr.parse_resp()
    return jsonify(dict_returned)
