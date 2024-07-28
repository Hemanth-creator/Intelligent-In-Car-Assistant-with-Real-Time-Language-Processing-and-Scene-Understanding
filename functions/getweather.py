import requests
api_key = "88662bbe37cd45acac390526242807"
import requests

def get_weather(location):
    api_key = '88662bbe37cd45acac390526242807'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no'

    # Make the GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        weather = response.json()
        return f"The current weather condition is {weather['current']['condition']['text']} with a temperature of {weather['current']['temp_c']}°C."
    else:
        return "Error"
