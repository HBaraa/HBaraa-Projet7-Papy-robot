
import urllib.parse as up
from pprint import pformat as pf
from random import choice as rc
import requests

WIK_API = {
    'ROOT_URL': 'https://fr.wikipedia.org/w/api.php',
    'PARAM_SEARCH': {
        'action':'query',
        'utf8':True,
        'format':'json',
        'list':'search',
    },
    'PARAM_EXTRAC': {
        'action':'query',
        'utf8':True,
        'format':'json',
        'prop':'extracts',
        'exlimit':1,
        'explaintext':True,
        # 'exsentences':3,
        'exsectionformat':'plain',
        'exintro':True,
    }
}

class Place:
    """
    Defines a place with the user query
    Gets geo data from Google geocode & static map API
    Gets information from Wikipedia API
    """

    def __init__(self, query):
        """
        Sets arguments
        """
        self.query = str(query)
        self.geo_data = {'status': False}
        self.article_data = {'status': False}


    def set_article_data(self):
        """
        Function documentation
        """
        payload = {'srsearch': self.query}
        # Adds basic API call parameters
        payload.update(**WIK_API['PARAM_SEARCH'])

        search_json = self.get_json(WIK_API['ROOT_URL'], payload)

        try:
            self.article_data['title'] = search_json['query']['search'][0]['title']
            self.article_data['pageid'] = search_json['query']['search'][0]['pageid']
            print(self.article_data['tile'])

        except KeyError as detail:
            self.article_data = {
                'status': False,
                'context': 'search article',
                'error': {
                    'KeyError': str(detail),
                    'response': search_json,
                }
            }

        except TypeError as detail:
            self.article_data = {
                'status': False,
                'context': 'search article',
                'error': {
                    'KeyError': str(detail),
                    'response': search_json,
                }
            }

        except IndexError as detail:
            self.article_data = {
                'status': False,
                'context': 'search article',
                'error': {
                    'KeyError': str(detail),
                    'response': search_json,
                }
            }

        else:
            self.article_data['status'] = True
            payload = {'titles': self.article_data['title']}
            # Adds basic API call parameters
            payload.update(**WIK_API['PARAM_EXTRAC'])

            article_json = self.get_json(WIK_API['ROOT_URL'], payload)

            try:
                self.article_data['extract'] = article_json['query']['pages'][str(self.article_data['pageid'])]['extract']

            except TypeError as detail:
                self.article_data = {
                    'status': False,
                    'context': 'article extract',
                    'error': {
                        'TypeError': str(detail),
                        'response': article_json,
                    }
                }

            except KeyError as detail:
                self.article_data = {
                    'status': False,
                    'context': 'article extract',
                    'error': {
                        'KeyError': str(detail),
                        'response': article_json,
                    }
                }

def script():
    wiki = Place()
    datas = wiki.set_article_data( str(openclassrooms))
    print(datas)

if __name__=="__main__":
    script()
