from dataclasses import dataclass
import numpy as np
import requests

@dataclass
class Point():
    def __init__(self, key, lat, lon):
        self.lat = lat
        self.lon = lon
        self.key = key
    
    def get_current_weather(self):
        # parameters of the api call for current weather
        params = dict(
            key = self.key, # personal key
            q = ",".join([str(self.lat),str(self.lon)]), # coordinates 
            aqi = "yes") # show data

        url = "http://api.weatherapi.com/v1/current.json?" # base url
        self.url = [str(key)+"="+str(value) for key, value in params.items()] # the rest of the url
        self.url = url + "&".join(self.url) # concatenating

        # making the request
        request_ = requests.get(self.url).json() 

        # setting variables to Point
        self.name = request_["location"]["name"]
        self.region = request_["location"]["region"]
        self.country = request_["location"]["country"]
        self.tz = request_["location"]["tz_id"]
        self.localtime_timestamp = request_["location"]["localtime_epoch"]
        self.localtime = request_["location"]["localtime"]
        self.last_updated = request_["current"]["last_updated"]
        self.temp_c = request_["current"]["temp_c"]
        self.is_day = request_["current"]["is_day"]
        self.condition = request_["current"]["condition"]["text"]
        self.condition_code = request_["current"]["condition"]["code"],
        self.wind_kph = request_["current"]["wind_kph"]
        self.wind_degree = request_["current"]["wind_degree"]
        self.wind_dir = request_["current"]["wind_dir"]
        self.pressure_mb = request_["current"]["pressure_mb"]
        self.precip_mm = request_["current"]["pressure_mb"]
        self.humidity = request_["current"]["humidity"]
        self.cloud = request_["current"]["cloud"]
        self.feelslike_c = request_["current"]["feelslike_c"]
        self.visibility_km = request_["current"]["vis_km"]
        self.gust_kph = request_["current"]["gust_kph"]


a = Point("e09bd02105a0402982d221246212809", -41.46574, -72.94289)
a.get_current_weather()
print(a.temp_c)

        
        #http://api.weatherapi.com/v1/current.json?key=e09bd02105a0402982d221246212809&q=-41.4657,-72.94289&aqi=yes