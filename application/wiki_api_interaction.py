import wikipedia
from flask import jsonify, request


def get_datas(keyword):
    wikipedia.set_lang("fr")
    datas = wikipedia.summary(keyword)
    # wikipedia page object is created
    page_object = wikipedia.page(keyword)
    # printing title
    title = page_object.original_title
    print(title)
    return datas
