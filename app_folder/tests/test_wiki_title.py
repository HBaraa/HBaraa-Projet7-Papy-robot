import requests

from ..papy_robot.wikipedia_api import ApiWikiTitle


def test_wikiapi(monkeypatch):
    result1 = {
        'batchcomplete': True,
        'query':
            {
                'geosearch': [{'pageid': 166033, 'ns': 0, 'title': "Jet d'eau de Genève", 'lat': 46.207388, 'lon': 6.155904, 'dist': 0.1, 'primary': True}]  # noqa
            }
    }

    class MockResponse:
        status_code = 200

        def json(self):
            return result1

    def mockWikipediaApi(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mockWikipediaApi)

    apiWiki = ApiWikiTitle({'lat': 46.2073889, 'lng': 6.1559028})

    assert apiWiki.title == "Jet d'eau de Genève"
