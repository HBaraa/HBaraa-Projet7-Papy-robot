import re
import wikipedia
import pytest


def getdata(keyword):
    wikipedia.set_lang("fr")
    datas = wikipedia.summary(keyword)
    print(datas)
    # print(type(datas))
    infos = str(datas)
    page_object = wikipedia.page(keyword)
    title = page_object.original_title
    print(title)
    return datas

def test_wiki_api():
    informations = getdata("openclassrooms")
    print(informations)
    print(type(informations))
    test_text = "OpenClassrooms est un site web de formation en ligne, créé en 1999 sous le nom de Site du Zéro. Il propose à ses membres des cours certifiants et des parcours débouchant sur des métiers en croissance. Initialement orientée autour de la programmation informatique, la plate-forme numérique couvre, depuis 2013, d'autres thématiques telles que l'entrepreneuriat et le marketing électronique. Ses formations sont dispensées selon le format MOOC."
    print(len(test_text))
    print(type(test_text))
    if re.match(test_text,informations):
        print("WELL DONE")
    else:
        print("FAILED")
    assert re.match(test_text,informations) == True

test_wiki_api()
