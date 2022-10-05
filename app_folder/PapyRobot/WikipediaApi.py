import requests


def get_wiki_title(coordinates):

    lat = coordinates["lat"]
    lng = coordinates["lng"]

    # ATTRIBUTE DATAS FOR URL
    api_begin = "https://fr.wikipedia.org/w/api.php?action=query"
    api_mid = "&list=geosearch&format=json&formatversion=2"
    api_coord = f"&gscoord={lat}|{lng}"
    api_param = "&gsradius=100&gslimit=1"

    # BUILD URL FOR REQUEST
    url = f"{api_begin}{api_mid}{api_coord}{api_param}"

    # REQUEST
    geo_data = requests.get(url).json()

    # ATTRIBUTE RESPONSE
    wiki_data = geo_data["query"]["geosearch"]

    # IF RESPONSE IS EMPTY RETURN NONE
    if len(wiki_data) == 0:
        return None
    # ELSE
    else:
        title = wiki_data[0]["title"]
        return title


def text_data(title):
    text_title = str(title)

    api_begin = "https://fr.wikipedia.org/w/api.php?action=query"
    api_mid = "&format=json&prop=extracts"
    api_title = f"&titles={text_title}"
    api_param = (
        "&formatversion=2&exsentences=3" +
        "&explaintext=1&exsectionformat=plain"
    )
    url = f"{api_begin}{api_mid}{api_title}{api_param}"

    extract_data = requests.get(url).json()
    # print(extract_data)
    anecdote = extract_data["query"]["pages"][0]
    # print(anecdote)
    if len(anecdote) <= 3:
        return None
    else:
        return anecdote["extract"]
