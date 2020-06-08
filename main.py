import requests
from secrets import WEATHER_API_KEY

def get_date():
    return "June 8, 2020"


def get_weather():
    url = "https://api.openweathermap.org/data/2.5/onecall"

    querystring = {
        "lat": "38.252666",
        "lon": "-85.758453",
        "exclude": "current,hourly",
        "appid": WEATHER_API_KEY,
        "units": "imperial"
    }

    payload = ""
    response = requests.request("GET", url, data=payload, params=querystring)
    weather_data = response.json()
    return """
# Weather
🌡 {} / {}
""".format(weather_data["daily"][0]["temp"]["min"], weather_data["daily"][0]["temp"]["max"])

def get_todos():
    return """
# Todo List
[] Feed dog
"""

def get_schedule():
    return """
Schedule
| Hour | Task        |
| ---- | ----------- |
| 9:00 | Read emails |
| 9:30 | asdf        |
"""


output = ""

output += get_date()
output += get_weather()
output += get_todos()
output += get_schedule()
print(output)
