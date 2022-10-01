# !/usr/bin/python3.8
# -*- coding: Utf-8 -*

"""
MAIN BOT SCRIPT
Utility :   Get datas to display geo_informations, greetings and anecdotes
Project :   GrandPy Bot, le papy robot
"""

import json

from app_folder.static.scripts.py_codes.utils import  text_parser
from app_folder.static.scripts.py_codes.api_access import get_map_info, get_wiki_data, get_text_data

class GrandPy:

    # CALLING FCTS TO ANALYSE USER_MESSAGE AND GET DATAS TO RETURN RESPONSE
    def get_response(self, msg):

        # Clean message
        user_message = text_parser(msg)
        # Initialize resp in json
        json_resp = {"map_data": "", "anecdote": "", "greetings": ""}

        # build response in json
        if len(user_message["msg"]) > 0:
            datas = self.get_datas(user_message["msg"])
            json_resp["map_data"] = datas[0]
            json_resp["anecdote"] = datas[1]
        else:
            json_resp["map_data"] = 0
            json_resp["anecdote"] = 0

        # In all case, say if they are greetings
        json_resp["greetings"] = user_message["greetings"]

        return json.dumps(json_resp, ensure_ascii=False, sort_keys=True)

    def get_datas(self, user_message):

        map_data = get_map_info(user_message)

        anecdote = "Désolé 🤷‍♂️ Mais je n'ai pas compris votre question ! 😇"

        if map_data is not None:
            wiki_data = get_wiki_data(map_data["coordinates"])
            anecdote = None
            if wiki_data is not None:
                anecdote = get_text_data(wiki_data)

        message = (map_data, anecdote)
        return message
