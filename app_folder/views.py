from flask import  Flask, render_template, jsonify, request
from flask.wrappers import Response
from http.client import HTTPResponse
from django.http import HttpRequest
from werkzeug.wrappers import response
from app_folder.utils import  text_parser
from .wiki_api import get_datas
from . import app
from app_folder.getting_infos import script
import cgi, cgitb

cgitb.enable()

data = cgi.FieldStorage()


@app.route("/")
def home():
    infos = ajax()
    print(infos)
    datas = get_datas("Lyon")
    print("******Youpyyyyy=====")
    data = cgi.FieldStorage()
    # print("Content-Type: text/html")
    # print(data)
    # HttpRequest.read(response)
    return render_template("home.html",
            informations = datas)


@app.route("/ajax", methods=["POST"])
def ajax():
        info = request.data.decode()
        # elemnt = HttpRequest.encoding
        # print(elemnt)
        response = text_parser(info)
        return jsonify(response)
