import requests
from typing import Dict, Any, List


def take_infos(title: str) -> Dict[str, Any]:
    params: Dict = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": title,
        }
    response = requests.get(
        'https://fr.wikipedia.org/w/api.php',
        params=params
    )
    if response.status_code == 200:
        print("DONE")
        datas = response.json()
        print(datas)
    else:
        pass

take_infos("openclassrooms")
