import wikipedia

def get_datas(keyword):
    wikipedia.set_lang("fr")
    datas = wikipedia.summary(keyword, sentences=5)
    print(datas)
    # print(type(datas))
    infos = str(datas)
    # all_elements = wikipedia.page(keyword).coordinates
    # elemnt = all_elements
    print("---------------------")
    # print(all_elements)
    print("************")
    # pt = re.compile(infos, flags = re.VERBOSE)
    # wikipedia page object is created
    page_object = wikipedia.page(keyword)
    # printing title
    title = page_object.original_title
    print(title)
    return datas

def get_wiki_title(self):
    lat = self.center[0]
    lng = self.center[1]
    # ATTRIBUTE DATAS FOR URL
    api_begin = "https://fr.wikipedia.org/w/api.php?action=query"
    api_mid = "&list=geosearch&format=json&formatversion=2"
    api_coord = f"&gscoord={lat}|{lng}"
    api_param = "&gsradius=100&gslimit=1"
    # BUILD URL FOR REQUEST
    url = f"{api_begin}{api_mid}{api_coord}{api_param}"
    # REQUEST
    geo_data = requests.get(url).json()
    print("-------------------------------_______________________")
    print(geo_data)
    print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    # ATTRIBUTE RESPONSE
    wiki_data = geo_data["query"]["geosearch"]
    # IF RESPONSE IS EMPTY RETURN NONE
    if len(wiki_data) == 0:
        return None
    # ELSE
    else:
        title = wiki_data[0]["title"]
        return title
