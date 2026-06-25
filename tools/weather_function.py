import requests
import os

def getWeather(location):
    weatherApi = os.getenv("WEATHER_API")
    if not weatherApi:
        return {"error": "WEATHER_API key not found in environment variables"}
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={weatherApi}'
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.Timeout:
        return {"error": "Weather API request timed out"}
    except requests.exceptions.HTTPError as e:
        return {"error": f"Weather API returned {e.response.status_code}: {e.response.text}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Weather API request failed: {e}"}