import requests

from .config import SECRET_KEY


class ApiGoogleAccess:
    def __init__(self, keyWord: str) -> str:

        """
            The ApiGoogleAccess class retrieves the address and a geographic
            coordinates linked to the keyWord.
            Args:
            keyWord (str): keyword is the data of the form that was parsed
            by the parse-text folder.
            Returns:
            str: the class returns the adress and the geographic coordinates
        """

        self.keyWord = keyWord
        self.urlMap = f"https://maps.googleapis.com/maps/api/geocode/json?address={self.keyWord}&key={SECRET_KEY}"   # noqa
        self.coords = {}
        self.adress = self.get_adress()

    def get_adress(self):
        if self.keyWord != "":
            response = requests.get(self.urlMap)
            if response.status_code == 200:
                content = response.json()
                if content["results"]:
                    print(content["results"])
                    add_data = content["results"][0]
                    place_adress = add_data["formatted_address"]
                    self.coords = add_data['geometry']['location']
                    return place_adress
                else:
                    return "Je n'ai pas compris ce que tu m'as dis mon poussin"
        else:
            return "Je n'ai pas compris ce que tu m'as dis mon poussin"

    def get_coordinates(self):
        return self.coords
