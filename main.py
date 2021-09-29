#@author: martin-conur

import requests
from datetime import datetime

# default 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

with open(".key", "r") as file:
    key = file.read()

lat, lon = -41.46574, -72.94289

def get_weather(lat:float, 
                lon:float, 
                key:str, 
                lang="en",
                units="metric")->dict:
    """Gets current weather data from openweathermap.org throught its API.
    
    Args:
        lat: Latitude in decimal degrees.

        lon : Longitude in decimal degrees.

        key: openweathermap API key, you have to have a subscription. 

        lang: Language of the returned data, prefer english, but if you want other, check https://openweathermap.org/current#multi

        units: Metric system to use, availables: 'kelvin', 'imperial' and 'metric'.
    
    Returns:
        JSON like Dictionary, with the current weather data.
    """

    params = dict(lat = lat,
                lon = lon,
                appid = key,
                lang= lang,
                units = units)

    # transforming params to strings and with the right format
    params_url = [str(key)+"="+str(value) for key, value in params.items()]
    # joining every params with the "&" operator
    params_url = "&".join(params_url)
    # concatenating base url with params url in order to get the full url
    full_url = base_url + params_url

    # http request
    r = requests.get(full_url)
    return r.json()



