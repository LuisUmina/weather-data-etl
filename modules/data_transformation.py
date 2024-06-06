import datetime

def transform_data(data):
    transformed_data = []
    for city_data in data:
        try:
            transformed = {
                'id': city_data['id'],
                'name': city_data['name'],
                'country': city_data['sys']['country'],
                'current_temp': city_data['main']['temp'],
                'feels_like': city_data['main']['feels_like'],
                'temp_min': city_data['main']['temp_min'],
                'temp_max': city_data['main']['temp_max'],
                'humidity': city_data['main']['humidity'],
                'wind_speed': city_data['wind']['speed'],
                'cloudiness': city_data['clouds']['all'],
                'weather_main': city_data['weather'][0]['main'],
                'timestamp': datetime.datetime.now()
            }
            transformed_data.append(transformed)
        except KeyError as e:
            print(f"Missing key in data: {e}")
    return transformed_data