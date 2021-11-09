import os
import random
import requests
import pprint
import urllib.parse
from typing import Any, Dict, List


class WikipediaApi:

    def __init__(self) -> None:
        self.wiki_url: str = "https://fr.wikipedia.org/w/api.php"

    def search_by_title(self, title: str) -> Dict[str, Any]:
        """Search for similar titles on Wiki API

        Args:
            title (str): Page title.

        Returns:
            Dict[str, Any]: Page ID and title of the API response page.
        """
        params: Dict = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": title,
        }
        req = requests.get(self.wiki_url, params=params)

        data = req.json()
        print(data)
        return {
            "page_id": data["query"]["search"][0]["pageid"],
            "title": data["query"]["search"][0]["title"],
        }

def script():
    wiki = WikipediaApi()
    datas ={}
    datas = wiki.search_by_title("tour Effel")
    print(datas)

if __name__=="__main__":
    script()
