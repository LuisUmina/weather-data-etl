import requests
import os

def extract_weather_data(api_url, API_KEY):
    cities = ['New York,US', 'London,GB', 'Tokyo,JP', 'Sydney,AU', 'Rio de Janeiro,BR', 
             'Moscow,RU', 'Cairo,EG', 'Beijing,CN', 'Cape Town,ZA', 'Mexico City,MX']
    all_data = []
    
    for city in cities:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        
        response = requests.get(api_url, params=params)
        
        if response.status_code == 200:
            all_data.append(response.json())
        else:
            print(f"Error {response.status_code} for {city}: {response.text}")
    
    return all_data