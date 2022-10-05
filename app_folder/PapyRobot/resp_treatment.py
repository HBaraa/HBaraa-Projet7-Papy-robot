from app_folder.PapyRobot.utils import text_parser, GREETING_LIST, detect_salutation, add_random_quotes
from app_folder.PapyRobot.GoogleApi import ApiGoogleAccess
from .wki_api import get_wiki_title, text_data


class ParseResponse:

    def __init__(self, info):
        self.info = info

    def parse_resp(self):
        response = text_parser(self.info)
        lat = 0
        lng = 0
        place = ""
        hyst = ""
        address = ""
        for word in response:
            message = detect_salutation(word)
        # print(message)
        if word in GREETING_LIST:
            response.remove(word)
        else:
            pass
        response_dict = {
            "reponse": response,
            "greeting": message["greeting_word"]
        }
        rep = response_dict["reponse"]
        # print(type(rep))
        if (len(rep) == 1) and (rep == ['']):
            pass
        else:
            rt = TreatResponse(rep)
            place, lat, lng, address, hyst = rt.resp_treat()
        if (place == ""):
            text_todisplay = None
            pass
        else:
            text_todisplay = add_random_quotes(place, hyst)
        dict_returned = {
            "reponse": response,
            "greeting": message["greeting_word"],
            "datas": text_todisplay,
            "place": place,
            "geodatas": [lng, lat],
            "address": address
        }
        return dict_returned


class TreatResponse:

    def __init__(self, rep):
        self.resp = rep

    def resp_treat(self):
        place = ""
        if (len(self.resp) == 1) and (self.resp == ['']):
            pass
        else:
            for (i, item) in enumerate(self.resp, start=1):
                # print(i, item)
                if item != "" or " ":
                    place += item
                    place += " "
                else:
                    pass
            # print(place)
            gaccess = ApiGoogleAccess(place)
            address = gaccess.get_adress()
            # print(address)
            geocoord = gaccess.get_coordinates()
            # print(geocoord)
            lat = geocoord["lat"]
            lng = geocoord["lng"]
            titlepl = get_wiki_title(geocoord)
            # print(titlepl)
            pdatas = text_data(titlepl)
            # print(pdatas)
            return place, lng, lat, address, pdatas

