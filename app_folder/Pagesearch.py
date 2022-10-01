import requests


def data_search(lat, lng):
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "query",
        "format": "json",
        "ggscoord": {lat} | {lng},
        "list": "geosearch",
        "gsradius": "10000"
    }
    R = S.get(url=URL, params=PARAMS)
    Data = R.json()
    places = Data['query']['pages']
    for k, v in places.items():
        print(str(v['title'])+": "+str(v['thumbnail']['source']))
    return None


data_search(45.7578137, 4.8320114)
