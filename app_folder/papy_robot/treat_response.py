from app_folder.papy_robot.parse_text import text_parser,GREETING_LIST, detect_salutation, add_random_quotes  # noqa
from app_folder.papy_robot.google_api import ApiGoogleAccess
from .wikipedia_api import ApiWikiTitle, WikipediaHistory


class ParseResponse:

    def __init__(self, info):
        """
            The ParseResponse class parse the text inputed
            by the user and retrieves a dictionary containing
            all informations that we need for our views.
            Args:
            info (str): info is the text entred by the user of
            the application witch contain the searched place.
            Returns:
            dict: the class returns the dictionary of
        """
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
        if word in GREETING_LIST:
            response.remove(word)
        else:
            pass
        response_dict = {
            "reponse": response,
            "greeting": message["greeting_word"]
        }
        rep = response_dict["reponse"]
        if (len(rep) == 1) and (rep == ['']):
            pass
        else:
            gd = TreatResponse(rep)
            place, lat, lng, address, hyst = gd.search_infos()
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
        """
            The TreatResponse class call methods of
            ApiGoogleAccess, ApiWikiTitle
            and WikipediaHistory and retrieves
            the name of the place, its longitude and its latitude,
            its address and informations about it.
        """
        self.resp = rep

    def search_infos(self):
        place = ""
        if (len(self.resp) == 1) and (self.resp == ['']):
            pass
        else:
            for (i, item) in enumerate(self.resp, start=1):
                if item != "" or " ":
                    place += item
                    place += " "
                else:
                    pass
            gaccess = ApiGoogleAccess(place)
            address = gaccess.get_adress()
            geocoord = gaccess.get_coordinates()
            lat = geocoord["lat"]
            lng = geocoord["lng"]
            wt = ApiWikiTitle(geocoord)
            titlepl = wt.get_wiki_title()
            wh = WikipediaHistory(titlepl)
            pdatas = wh.text_data()
            return place, lng, lat, address, pdatas
