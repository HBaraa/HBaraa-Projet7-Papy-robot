from app_folder.papy_robot.parse_text import text_parser, detect_salutation, add_random_quotes  # noqa
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
        message = {}
        dict_returned = {}
        for word in response:
            message = detect_salutation(word)
            response_dict = {
                "reponse": response,
                "greeting": message["greeting_word"]
            }
            rep = response_dict["reponse"]
            if (len(rep) == 1) and (rep == ['']):
                pass
            else:
                gd = TreatResponse(rep)
                title, place, lng, lat, address, hyst = gd.search_infos()   # noqa
            if (place == ""):
                text_todisplay = None
                pass
            else:
                text_todisplay = add_random_quotes(place, hyst)
        try:
            dict_returned = {
                "reponse": response,
                "greeting": message["greeting_word"],
                "datas": text_todisplay,
                "place": place,
                "geodatas": [lng, lat],
                "address": address,
                "title": title
                }
        except KeyError:
            dict_returned = {
                "reponse": "",
                "greeting": "",
                "datas": "",
                "place": "",
                "geodatas": [0, 0],
                "address": "",
                "title": ""
                }
            pass
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
        self.info_status = True

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
            # print(address)
            try:
                geocoord = gaccess.get_coordinates()
                lat = geocoord.get("lat")
                lng = geocoord.get("lng")
            except KeyError:
                pass
            wt = ApiWikiTitle(geocoord)
            titlepl = wt.get_wiki_title()
            wh = WikipediaHistory(titlepl)
            pdatas = wh.text_data()
            return titlepl, place, lat, lng, address, pdatas
