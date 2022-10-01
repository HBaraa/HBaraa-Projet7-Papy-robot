from .wikipediapy import get_datas

def script():
    infos = get_datas("openclassrooms")
    print(infos)



