from flask import  Flask, render_template, jsonify, request
from application.utils import  text_parser
from .wiki_api_interaction import get_datas
from . import app
from .getting_infos import script


@app.route("/")
def home():
    description = ajax()
    details = get_datas(description)
    return render_template("home.html",
        eplay = description,
        information = details,
        blur = True)

@app.route("/ajax", methods=["POST"])
def ajax():
        info = request.data.decode()
        response = text_parser(info)
        print(response)
        return jsonify(response)
