import requests

from .config import SECRET_KEY


class ApiGoogleAccess:
    def __init__(self, keyWord: str) -> str:

        """ The api_map class retrieves the address and a geographic map linked to the keyWord.
            Args:
            keyWord (str): keyword is the data of the form that was parsed by the user_question class.

            Returns:
                str: the class returns the address and a geographic map or image of GrandPy with an error message.
        """

        self.keyWord = keyWord
        self.urlMap = f"https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key=AIzaSyCRyU2shTW0xbnr_-3hjim_E1K9pE0G4LQ"
        self.adress = self.get_adress()
        self.coordinates = self.get_coordinates()
        self.adressMap = self.get_adress_map()
        self.imgMap = self.get_imgMap()

    def get_adress(self):
        if self.keyWord != "":
            response = requests.get(self.urlMap)
            if response.status_code == 200:
                content = response.json()
                if content['results'] != []:
                    return content["results"][0]['formatted_address']
                else:
                    return "Je n'ai pas compris ce que tu m'as dis mon petit"
        else:
            return "Je n'ai pas compris ce que tu m'as dis mon petit"

    def get_coordinates(self):
        response = requests.get(self.urlMap)
        response = response.json()
        result = response['results'][0]
        coordinates = []
        coordinates[0] = result['geometry']['location']['lat']
        coordinates[1] = result['geometry']['location']['lng']
        return coordinates

if __name__ == "__main__":
    apiAccess = ApiGoogleAccess("")
    print(apiAccess.keyWord)
    print(apiAccess.adress)
    print(apiAccess.coordinates)
    # print(apiMap1.adressMap)
    print(apiAccess.urlMap)
    # print(apiMap1.imgMap)


# def get_adress_map(self):
    #    adressMap = str(self.adress)
    #    adressMap = adressMap.replace(" ", "+")
    #    return adressMap

    # def get_imgMap(self):
    #   print(self.adressMap)
    #    if self.adressMap != "Je n'ai pas compris ce que tu m'as dis mon petit".replace(" ", "+"):
    #       return f"""https://maps.googleapis.com/maps/api/staticmap?center={self.adressMap}&zoom=13&size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318&markers=color:red%7Clabel:C%7C40.718217,-73.998284&key={apiKeyMap}"""
    #    else:
    #       return "static/images/grandpapy.png"
