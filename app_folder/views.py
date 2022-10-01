from csv import excel
from flask import  Flask, render_template, jsonify, request
from flask.wrappers import Response
from http.client import HTTPResponse
from django.http import HttpRequest
import json
import str
import string
from werkzeug.wrappers import response

from app_folder.PapyRobot.wiki_api_2 import fromcoordtoplace
from app_folder.PapyRobot.utils import text_parser, GREETING_LIST, detect_salutation, is_empty, filtred_text, add_random_quotes
from app_folder.PapyRobot.wikipediapy import get_datas
from . import app
from app_folder.PapyRobot.getting_infos import script
from app_folder.coord_geo import CreaMap
from app_folder.PapyRobot.WikipediaApi import ApiWikiMedia, search_page_by_geo
# from app_folder.PapyRobot.wki_api import get_wiki_title, text_data


@app.route("/")
def home():
    infos = ajax()
    # print(type(infos))
    # print(infos)
    print("******Youpyyyyy=====")
    return render_template("home.html")


@app.route("/ajax", methods=["POST"])
def ajax():
    lat = 0
    lng = 0
    place = ""
    hyst = ""
    info = request.data.decode()
    response = text_parser(info)
    print(type(response))
    for word in response:
        message = detect_salutation(word)
        print(message)
        if word in GREETING_LIST:
            response.remove(word)
        else:
            pass
    response_dict = {
            "reponse": response,
            "greeting": message["greeting_word"]
    }
    print("******")
    rep = response_dict["reponse"]
    # print(len(rep), rep)
    print("hellooo")
    print(rep)
    print(len(rep))
    place = ""
    if (len(rep) == 1) and (rep == ['']):
    #     print("loooooooooooooser")
        pass
    else:
        for (i, item) in enumerate(rep, start=1):
            print(i, item)
            if item != "" or " ":
                place += item
                place += " "
            else:
                pass
        place.strip()
        print("OOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!OOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        print(place)
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        wk = ApiWikiMedia(place)
        hyst = wk.get_content()
        print(hyst)
        cm = CreaMap(place)
        lat, lng = cm.foundcoords()
        # title_todisplay = get_wiki_title({"lat": lat, "lng": lng})
        geocoord = {"lat": lat, "lng": lng}
        print(geocoord)
        print(place)
        if (geocoord != {}):
            print("???????????§§§§§§§§§§§§§§§§§§!!!!!!!!!!!!!!!!!!!!")
            cods = search_page_by_geo(place, geocoord)
            print(cods)
            title_todisplay = cods["title"]
            print(title_todisplay)
            print("6666666666666666666666666669999999999999999999999999")
            pass
        else:
            print("NNNNOOOOOOOOOOOPE")
            pass
        print("5555555555555555555555555555555555")
        print(title_todisplay)
        print(place)
        print(type(place))
        print("5555555555555555555555555555555555")
    # searched_title = filtred_text(place)
    # print("5555555555555555555555555555555555")
    # print(searched_title)
    # print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    # print(type(searched_title))
    # print(type(searched_title))
    if (place == ""):
        text_todisplay = None
        pass
    else:
        text_todisplay = add_random_quotes(place, hyst)


    dict_returned = {
        "reponse": response,
        "greeting": message["greeting_word"],
        "datas": text_todisplay,
        "place": place,
        "geodatas": [lng, lat]
    }
    return jsonify(dict_returned)




