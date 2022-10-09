import requests

from ..papy_robot.wikipedia_api import WikipediaHistory


def test_wikihistory(monkeypatch):

    result = {
        'batchcomplete': True,
        'query':
            {
                'pages':
                [
                    {
                        'pageid': 166033,
                        'ns': 0,
                        'title': "Jet d'eau de Genève",
                        'extract': "Le jet d'eau de Genève est un jet d'eau vertical d'une hauteur de 140 mètres situé dans la rade de Genève, en Suisse. Véritable emblème de la ville, il s’agit de l'un de ses principaux attraits touristiques depuis 1891.\n\n\nHistoire\n\n\nOrigine\n\nAu XIXe siècle, Genève se développe de manière importante : de 64 000 habitants en 1850, elle passe à plus de 100 000 en 1890."  # noqa
                    }
                ]
            }
        }
    datas = result["query"]["pages"][0]

    class MockResponse:
        status_code = 200
        len(datas) >= 3

        def json(self):
            return result

    def mockWikipediaApi(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mockWikipediaApi)

    apiWiki = WikipediaHistory("Jet d'eau de Genève")

    assert apiWiki.infos == datas["extract"]
