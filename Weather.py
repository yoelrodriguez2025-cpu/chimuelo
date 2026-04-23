import requests
import shutil
import json

class Weather:
    """
    Create account and get your api key
    https://openweathermap.org/api
    """
    def get_weather(self, city, api_key):
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        params = {"q": city, "appid": api_key, "units": "metric"}

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()

            weather_data = response.json()

            if weather_data["cod"] == 200:
                print(f" Weather in {weather_data['name']}:")
                print(f" Description: {weather_data['weather'][0]['description']}")
                print(f" Temperature: {weather_data['main']['temp']}°C")
                print(f" Humedity: {weather_data['main']['humidity']}%")
                print(f" Wind Speed: {weather_data['wind']['speed']} m/s")
            else:
                print(f"Error: {weather_data['message']}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
        except json.JSONDecodeError:
            print("Error: Could not decode JSON response")
    
api_key = "2419bb362c43bc6ec3b78de6045acbba"
city = ""
