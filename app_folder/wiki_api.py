import wikipedia
from flask import json, jsonify, request


def get_datas(keyword):
    wikipedia.set_lang("fr")
    datas = wikipedia.summary(keyword)
    print(datas)
    # print(type(datas))
    infos = str(datas)
    # pt = re.compile(infos, flags = re.VERBOSE)
    # wikipedia page object is created
    page_object = wikipedia.page(keyword)
    # printing title
    title = page_object.original_title
    print(title)
    return datas

