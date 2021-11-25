import json
import re
import requests
from pprint import pprint


URL =  "https://www.mediawiki.org/wiki/API:Main_page/fr"
def get_products() -> list:
    datas = requests.get(
        URL,
    )
    prod = datas.text
    products = json.dumps(prod,indent=4, separators=(". ", " = "))
    if datas.status_code == 200:
        print("Success!")
    elif datas.status_code == 404:
        print("DATA Not Found.")
    # prods = datas.json()
    # pprint(prods)
    # if prods:
        # print("*********____DONE____*******")
        # pass
    prods = datas
    print(type(datas))
    print(type(prod))
    print(type(products))
    pprint(prods)
    # pprint(datas)
    # pprint(prod)
    return products

get_products()
