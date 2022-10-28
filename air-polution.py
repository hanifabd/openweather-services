import requests

# openweathermap.org
def get_airpollution(lat, lon, api_key):
    airpollution_information = requests.get(
        "http://api.openweathermap.org/data/2.5/air_pollution",
        params = {
            'lat': lat,
            'lon': lon,
            'appid': api_key,
        },
        headers = {}
    ).json()

    return airpollution_information

# Output Json
'''
{
    'coord': {
        'lon': 111.4242, 
        'lat': -6.9713
    }, 
    'list': [
        {
            'main': {
                'aqi': 1
            }, 
            'components': {
                'co': 333.79, 
                'no': 0.04, 
                'no2': 3.43, 
                'o3': 67.95, 
                'so2': 2.47, 
                'pm2_5': 6.09, 
                'pm10': 9.91, 
                'nh3': 5.83
            }, 
            'dt': 1666948777
        }
    ]
}
'''

print(get_airpollution(-6.9712803, 111.4242222, "0d604e23805adaefd99a77ea157a414b"))
