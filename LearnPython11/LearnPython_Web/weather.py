import requests

def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params =  {
        "key": "9c11fab56d2d460791b184847191111",
        "q": "Yekaterinburg, Russia",
        "format": "json",
        "num_of_days": 1,
        "lang": "ru",
        "date": "dd-MM-yyyy",
    }    
    result = requests.get(weather_url, params=params)
    weather = result.json()
    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False
    return False

if __name__ == "__main__":
    print(weather_by_city("Yekaterinburg, Russia"))
