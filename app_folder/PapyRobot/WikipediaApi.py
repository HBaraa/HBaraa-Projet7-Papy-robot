#! /usr/bin/env python3
# coding utf-8

import requests
import pprint
from typing import Dict, Any


class ApiWikiMedia:
    def __init__(self, keyWord) -> None:
        """This class retrieves datwa from the wikipedia API

        Args:
            keyWord (str): the keyword is the incoming data for the wikipedia API.

        Returns:
            The api_wikipedia class returns a little story or an error message if the input data is incorrect.
        """
        self.keyWord = keyWord
        self.url = f"https://fr.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles={self.keyWord}"
        self.history = self.get_content()

    def get_content(self):
        if self.keyWord != "":
            content = requests.get(self.url)
            if content.status_code == 200:
                history = content.json()
                print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
                pp = pprint.PrettyPrinter(indent=2)
                pp.pprint(history)
                #  print(history)
                print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
                pageid = str(history["query"]["pages"])
                pageid = pageid.split("{")[1][1:-3]
                if int(pageid) != -1:
                    history = str(history["query"]["pages"][pageid]["extract"])
                    if history != "":
                        history = str(history.split(".")[0:2])[2:-2]
        return history


def search_page_by_geo(place, coords: Dict[str, float]) -> Dict[str, Any]:
    """Search and returns a random page near the given coords.

    Args:
        coords (str): Location Coords.

    Returns:
        Dict[str, Any]: Page ID and title of the API response page.
    """
    lat = str(coords["lat"])
    lng = str(coords["lng"])
    url = f"https://fr.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles={place}"
    params: Dict = {
        "action": "query",
        "format": "json",
        "list": "geosearch",
        "gscoord": f"{lat}|{lng}",
    }
    req = requests.get(url, params=params)
    info = req.json()
    print(info["query"]["geosearch"])
    if (info["query"]["geosearch"] != []):
        data = info["query"]["geosearch"][0]
        dicgeo = {
            "page_id": data["pageid"],
            "title": data["title"],
        }
        return dicgeo
    else:
        return {}


def extract_title(place):
    rennes = ApiWikiMedia(place)
    print(rennes.url)
    print(rennes.history)
#    infodic = search_page_by_geo(place, coords)
#    print(infodic)

extract_title("poste nancy")
# , {"lat": 45.7578137, "lng": 4.8320114}
