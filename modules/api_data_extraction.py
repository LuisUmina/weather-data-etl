import requests
import os

def get_weather_data(api_url, API_KEY):   
    cities = [
    'New York,US', 'London,GB', 'Tokyo,JP', 'Sydney,AU', 'Rio de Janeiro,BR', 
    'Moscow,RU', 'Cairo,EG', 'Beijing,CN', 'Cape Town,ZA', 'Mexico City,MX',
    'Paris,FR', 'Berlin,DE', 'Madrid,ES', 'Rome,IT', 'Toronto,CA',
    'Buenos Aires,AR', 'Sao Paulo,BR', 'Lima,PE', 'Bogota,CO', 'Caracas,VE',
    'Jakarta,ID', 'Bangkok,TH', 'Seoul,KR', 'Manila,PH', 'Singapore,SG',
    'Kuala Lumpur,MY', 'Hanoi,VN', 'Mumbai,IN', 'Delhi,IN', 'Istanbul,TR',
    'Los Angeles,US', 'Chicago,US', 'Houston,US', 'Phoenix,US', 'Philadelphia,US',
    'San Antonio,US', 'San Diego,US', 'Dallas,US', 'San Jose,US', 'Austin,US',
    'Miami,US', 'Atlanta,US', 'Boston,US', 'Seattle,US', 'Denver,US',
    'Las Vegas,US', 'Portland,US', 'Minneapolis,US', 'Orlando,US', 'Detroit,US',
    'San Francisco,US', 'Washington,US', 'Osaka,JP', 'Shanghai,CN', 'Chongqing,CN',
    'Bangkok,TH', 'Hanoi,VN', 'Kuala Lumpur,MY', 'Manila,PH', 'Jakarta,ID'
    ]

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