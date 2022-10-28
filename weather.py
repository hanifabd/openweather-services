import requests

# openweathermap.org
def get_weather(lat, lon, lang, api_key):
    weather_information = requests.post(
        "https://api.openweathermap.org/data/2.5/weather",
        params = {
            'lat': lat,
            'lon': lon,
            'lang': lang,
            'appid': api_key,
        },
        headers = {}
    ).json()

    return weather_information

# Output Json
'''
{
    'coord': {
        'lon': 111.4242, 
        'lat': -6.9713
    }, 
    'weather': [
        {
            'id': 804, 
            'main': 'Clouds', 
            'description': 'awan mendung', 
            'icon': '04d'
        }
    ], 
    'base': 'stations', 
    'main': {
        'temp': 302.75, 
        'feels_like': 304.88, 
        'temp_min': 302.75, 
        'temp_max': 302.75, 
        'pressure': 1006, 
        'humidity': 58, 
        'sea_level': 1006, 
        'grnd_level': 996
    }, 
    'visibility': 10000, 
    'wind': {
        'speed': 4.71, 
        'deg': 237, 
        'gust': 4.99
    }, 
    'clouds': {
        'all': 100
    }, 
    'dt': 1666943868, 
    'sys': {
        'country': 'ID', 
        'sunrise': 1666908487, 
        'sunset': 1666952875
    }, 
    'timezone': 25200, 
    'id': 1648568, 
    'name': 'Blora', 
    'cod': 200
}
'''

print(get_weather(-6.9712803, 111.4242222, "id", "0d604e23805adaefd99a77ea157a414b"))