## wapi: Weather API

wapi is a simple python library that allows you to get weather data from weatherapi.com,
you just need to have a key (free access)

### Installation
    pip install wapi

### Using wapi

   ```python 
   #!/usr/bin/env python

    from wapi import WeatherPoint

    # set a point of interest where we want to get weather data from
    key = {VALID KEY}
    latitude = -33.9
    longitude = 50.48

    point = WeatherPoint(key, latitude, longitude)

    # get current weather data
    point.get_current_weather()

    # access to specific weather data

    point.temp_c # temperature in celsius
    point.wind_kmh # wind in kilometers per hour
    point.localtime # local datetime of the request

    # soon all the docs availables
```


Visit and contribute to our Github repo <url>https://github.com/martin-conur/wapi</url>
