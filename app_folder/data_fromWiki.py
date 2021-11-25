import json
import requests as req
import re
import pprint
import urllib
import urllib.request

def request_api(url):
    """Request the selected url and return data from the api as json"""
    data = req.get(url)
    return data.json()

def get_title_from_wiki(keywords):
    """Request media wiki to get the title of the first article link to the keywords"""
    #Return all the articles link to the keywords
    url = 'https://fr.wikipedia.org/w/api.php?action=opensearch&search={}'.format(keywords)
    data = request_api(url)
    #Try to get and return the firt article
    try:
        article_title = data[1][0]
    #Return an error message if there is no result
    except IndexError:
        msg_error = "Euh... Non en fait je ne connais rien d'intéressant à ce sujet."
        return msg_error
    return article_title


def get_data_from_wiki(keywords):
    """Request wikimedia to get the firt sentences of a wikipedia article"""
    article_title = get_title_from_wiki(keywords)
    #Return the first sentence of a wikipedia article
    url = 'https://fr.wikipedia.org/w/api.php?action=query&titles={}&prop=extracts&exsentences=1'.format(article_title)
    response = urllib.request.urlopen(url)
    print(type(response))
    strr = str(response)
    print(strr)
    # jsonResponse = json.loads(response)
    # print(type(jsonResponse))
    strr = str(response)
    # print(strr)
    print(type(strr))
    # link = url = json.loads(data.text)["updates"][0][url]
    # print(link)
    # print(data["query"]["pages"].values()[0]["extract"])
    #Loop on only one element (page_id), but usefull because we don't know the id of the page
    # for page_id in data['query']['pages']:
    #     result = data['query']['pages'][page_id]['extract']
    return "trying to resolve it"

def scnd_script():
    datas = get_data_from_wiki("openclassrooms")
    print(datas)

if __name__ == "__main__":
    scnd_script()
