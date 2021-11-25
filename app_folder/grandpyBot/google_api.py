﻿import os
import requests
from typing import Dict


class GoogleMapsApi:
    """Google Maps API interaction class.
    """

    def __init__(self) -> None:
        """The GoogleMapsApi Constructor
        """
        self.google_maps_api_url: str = "https://maps.googleapis.com/maps/api/geocode/json"
        self.payloads: Dict = {
            "key": os.environ.get("GOOGLE_API_KEY"),
            "region": "fr",
            "address": "",
        }

    def search(self, query: str) -> Dict[str, float]:
        """From a query return a dictionary containing latitude and longitude.
        Args:
            query (str): A string containing the query.
        Returns:
            Dict[str, float]: The location of the searched place.
        """
        data = self._request(query)

        return {
            "address": data["results"][0]["formatted_address"],
            "coords": data["results"][0]["geometry"]["location"],
        }

    def _request(self, query: str) -> Dict[str, float]:
        """Query the Google Geocode API and returns the coords of the requested address.
        
        Args:
            query (str): The address requested by the user.
        Returns:
            Dict[str, float]: The location of the requested place.
        """
        self.payloads["address"] = query
        req = requests.get(self.google_maps_api_url, params=self.payloads)
        return req.json()
