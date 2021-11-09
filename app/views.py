from flask import  Flask, render_template, jsonify, request
import json
from werkzeug.wrappers import response
from django.shortcuts import render
from django.http import HttpResponse
from utils import  text_parser
from wiki_api_interaction import get_datas
from application import script


app = Flask(__name__)


@app.route("/")
def home():
    description = ajax()
    details = script()
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

