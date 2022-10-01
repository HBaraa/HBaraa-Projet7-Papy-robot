import os
from geopandas.tools import geocode
import folium
import requests
import random
import urllib.parse
import json
from typing import Any, Dict, List
from bokeh.io import output_notebook
from branca.element import Figure
from app_folder.PapyRobot.wiki_api_2 import fromcoordtoplace
from app_folder.PapyRobot.wki_api import get_wiki_title


class CreaMap():

    def __init__(self, place_to_find):
        self.place = place_to_find
        self.lat = 0
        self.lon = 0
        self.center = []

    def foundcoords(self):
        geo_datas = geocode(self.place, provider='nominatim', user_agent='xyz', timeout=5)
        print(geo_datas)
        info_point = geo_datas["geometry"][0]
        print(info_point)
        address = geo_datas["address"][0]
        print(address)
        print(info_point.coords)
        coordinates = list(info_point.coords)[0]
        print(coordinates)
        self.lat = coordinates[0]
        self.lon = coordinates[1]
        print(self.lat)
        print(self.lon)
        # title_todisplay = fromcoordtoplace(lat, lon)
        # print(title_todisplay)
        return self.lat, self.lon




