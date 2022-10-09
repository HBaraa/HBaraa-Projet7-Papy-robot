import requests

from ..papy_robot.google_api import ApiGoogleAccess


def test_apigoogle(monkeypatch):
    results = {
        'results':
            [
                {
                    'address_components':
                        [
                            {
                                'long_name': 'The Geneva Water Fountain',
                                'short_name': 'The Geneva Water Fountain',
                                'types': ['establishment', 'park', 'point_of_interest', 'tourist_attraction']  # noqa
                            },
                            {'long_name': 'Quai Gustave-Ador', 'short_name': 'Quai Gustave-Ador', 'types': ['route']},  # noqa
                            {'long_name': 'Genève', 'short_name': 'Genève', 'types': ['locality', 'political']},    # noqa 
                            {'long_name': 'Genève', 'short_name': 'Genève', 'types': ['administrative_area_level_2', 'political']},   # noqa
                            {'long_name': 'Genève', 'short_name': 'GE', 'types': ['administrative_area_level_1', 'political']},    # noqa
                            {'long_name': 'Switzerland', 'short_name': 'CH', 'types': ['country', 'political']},  # noqa
                            {'long_name': '1207', 'short_name': '1207', 'types': ['postal_code']}   # noqa
                        ],
                        'formatted_address': 'The Geneva Water Fountain, Quai Gustave-Ador, 1207 Genève, Switzerland',   # noqa
                        'geometry':
                            {
                                'location': {'lat': 46.2073889, 'lng': 6.1559028},   # noqa
                                'location_type': 'GEOMETRIC_CENTER',
                                'viewport':
                                    {
                                        'northeast': {'lat': 46.2078022302915, 'lng': 6.158073930291502}, # noqa
                                        'southwest': {'lat': 46.20510426970851, 'lng': 6.155375969708498}  # noqa
                                    }
                            },
                            'partial_match': True,
                            'place_id': 'ChIJxYdJYjpljEcRSJJQjwS5fwM',
                            'plus_code': {'compound_code': '6544+X9 Geneva, Switzerland', 'global_code': '8FR86544+X9'},   # noqa
                            'types': ['establishment', 'park', 'point_of_interest', 'tourist_attraction']   # noqa
                }
            ]
    }

    class MockResponse:
        status_code = 200

        def json(self):
            return results

    def mockApiGooGle(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mockApiGooGle)
    GoogleAccess = ApiGoogleAccess("Jet d'eau de Genève")

    assert GoogleAccess.adress == 'The Geneva Water Fountain, Quai Gustave-Ador, 1207 Genève, Switzerland'  # noqa
    assert GoogleAccess.get_coordinates() == {'lat': 46.2073889, 'lng': 6.1559028}  # noqa
