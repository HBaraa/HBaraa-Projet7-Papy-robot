import pandas as pd
import requests
import geopandas as gpd
import folium
import seaborn as sns
from IPython.display import display

code_commune="01450"
size = 100
api_root="https://koumoul.com/data-fair/api/v1/datasets/dpe-france/lines"
url_api = f"{api_root}?page=1&after=10&format=json&q_mode=simple&qs=code_insee_commune_actualise" + "%3A%22" + f"{code_commune}" + "%22" + f"&size={size}&select=" + "%2A&sampling=neighbors"

import requests
import pandas as pd

req = requests.get(url_api)
wb = req.json()

print(req.content[:1000])

def get_dpe_from_url(url):

    req = requests.get(url)
    wb = req.json()
    df = pd.json_normalize(wb["results"])

    dpe = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude), crs = 4326)
    dpe = dpe.dropna(subset = ['longitude', 'latitude'])
    print(type(dpe))
    print(dpe)
    return dpe
dpe = get_dpe_from_url(url_api)
dpe.head(2)

palette = sns.color_palette("coolwarm", 8)

def interactive_map_dpe(dpe):

    # convert in number
    dpe['color'] = [ord(dpe.iloc[i]['classe_consommation_energie'].lower()) - 96 for i in range(len(dpe))]
    dpe = dpe.loc[dpe['color']<=7]
    dpe['color'] = [palette.as_hex()[x] for x in dpe['color']]


    center = dpe[['latitude', 'longitude']].mean().values.tolist()
    sw = dpe[['latitude', 'longitude']].min().values.tolist()
    ne = dpe[['latitude', 'longitude']].max().values.tolist()

    m = folium.Map(location = center, tiles='Stamen Toner')

    # I can add marker one by one on the map
    for i in range(0,len(dpe)):
        folium.Marker([dpe.iloc[i]['latitude'], dpe.iloc[i]['longitude']],
                    popup=f"Année de construction: {dpe.iloc[i]['annee_construction']}, <br>DPE: {dpe.iloc[i]['classe_consommation_energie']}",
                    icon=folium.Icon(color="black", icon="home", icon_color = dpe.iloc[i]['color'])).add_to(m)

    m.fit_bounds([sw, ne])
    print(m)
    x_median = dpe['longitude'].median()
    y_median = dpe['latitude'].median()
    param_distance = f'{x_median},{y_median},1000'
    print(param_distance)
    url_api = f"{api_root}?page=1&after=10&format=json&q_mode=simple&qs=code_insee_commune_actualise" + "%3A%22" + f"{code_commune}" + "%22" + f"&size={size}&select=" + "%2A&sampling=neighbors" + f"&geodistance={param_distance}"
    print(url_api)
    dpe_geo_filter = get_dpe_from_url(url_api)
    print(dpe_geo_filter)
    print(type(dpe_geo_filter))
    print(dpe_geo_filter)
    # m_geo_filter = interactive_map_dpe(dpe)
    # print(m_geo_filter)
    map_osm = folium.Map(location=[45.5236, -122.6750])
    # map_osm.create_map(path='osm.html')

    return m

m = interactive_map_dpe(dpe)
display(m)
