from turtle import title
import requests


class ApiWikiTitle:

    def __init__(self, coordinates):
        """
            The ApiWikiTitle class retrieves the title linked to geographic
            coordinates.
            Args:
            coordinates (dict): coordinates is the dictionnary .
            Returns:
            str: the class returns the title of the page wikipedia searched
        """
        self.coordinates = coordinates
        self.title = self.get_wiki_title()

    def get_wiki_title(self):

        lat = self.coordinates.get("lat")
        lng = self.coordinates.get("lng")

        # ATTRIBUTE DATAS FOR URL
        api_begin = "https://fr.wikipedia.org/w/api.php?action=query"
        api_mid = "&list=geosearch&format=json&formatversion=2"
        api_coord = f"&gscoord={lat}|{lng}"
        api_param = "&gsradius=100&gslimit=1"

        # BUILD URL FOR REQUEST
        url = f"{api_begin}{api_mid}{api_coord}{api_param}"

        # REQUEST
        geo_data = requests.get(url).json()

        # ATTRIBUTE RESPONSE
        try:
            wiki_data = geo_data["query"]["geosearch"]
        except KeyError:
            wiki_data = "Excuse-moi mon petit je n'est pas trouvé l'adresse"
            print(wiki_data)

        # IF RESPONSE IS EMPTY RETURN NONE
        try:
            if len(wiki_data) == 0:
                pass
                return None
            else:
                self.title = wiki_data[0]["title"]
        except TypeError:
            self.title = ""
        return self.title


class WikipediaHistory:
    def __init__(self, searched_title):
        """
            The WikipediaHistory class retrieves informations about the title
            searched.
            Args:
            title (str): The title of the page Wikipedia.
            Returns:
            str: the class returns the history (informations)
            of the title searched.
        """
        self.title = searched_title
        self.anecdote = ""
        self.infos = self.text_data()

    def text_data(self):
        text_title = str(self.title)
        api_begin = "https://fr.wikipedia.org/w/api.php?action=query"
        api_mid = "&format=json&prop=extracts"
        api_title = f"&titles={text_title}"
        api_param = (
                        "&formatversion=2&exsentences=3" +
                        "&explaintext=1&exsectionformat=plain"
        )
        url = f"{api_begin}{api_mid}{api_title}{api_param}"
        extract_data = requests.get(url).json()
        try:
            self.anecdote = extract_data["query"]["pages"][0]
        except KeyError:
            self.anecdote = ""
        if len(self.anecdote) <= 3:
            return None
        else:
            self.infos = self.anecdote["extract"]
        return self.infos
