import wikipedia

def fromcoordtoplace(lon, lat):
    wikipedia.set_lang("fr")
    info_founded = wikipedia.geosearch(lon, lat)
    print(info_founded)
    print(info_founded[3])
    return info_founded


#fromcoordtoplace(45.7578137, 4.8320114)
