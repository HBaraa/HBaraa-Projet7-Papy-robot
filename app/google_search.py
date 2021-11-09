import googlemaps
from config import SECRET_KEY

acces_api = googlemaps.Client(SECRET_KEY)
coord_gps = acces_api.geocode("Openclassrooms")
