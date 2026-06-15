import requests
import os

def getWeather(location):
    weatherApi = os.getenv("WEATHER_API")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={weatherApi}'
    
    res = requests.get(url)
    return res.json()