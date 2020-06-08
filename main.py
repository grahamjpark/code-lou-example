import requests
from datetime import datetime
import pyperclip
from secrets import WEATHER_API_KEY

def get_date():
    return str(datetime.today().strftime('%B %d, %Y'))


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
    with open("schedule.md") as f:
        schedule = f.read()
        return """
# Schedule
{}
    """.format(schedule)


output = ""

output += get_date()
output += get_weather()
output += get_todos()
output += get_schedule()
pyperclip.copy(output)