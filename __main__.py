import os
from modules.upload_rs import load_data_to_redshift
from modules.data_transformation import transform_data
from modules.data_from_api import extract_weather_data
from parameters import base_url
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def main():
    API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

    if not API_KEY:
        logging.error("No API key found. Please set the OPENWEATHERMAP_API_KEY environment variable.")
        return

    REDSHIFT_USERNAME = os.getenv('REDSHIFT_USERNAME')
    REDSHIFT_PASSWORD = os.getenv('REDSHIFT_PASSWORD')
    REDSHIFT_HOST = os.getenv('REDSHIFT_HOST')
    REDSHIFT_PORT = os.getenv('REDSHIFT_PORT')
    REDSHIFT_DBNAME = os.getenv('REDSHIFT_DBNAME')

    raw_data = extract_weather_data(base_url,API_KEY)
    transformed_data = transform_data(raw_data)
    df = pd.DataFrame(transformed_data)
    redshift_conn_str = f'redshift+psycopg2://{REDSHIFT_USERNAME}:{REDSHIFT_PASSWORD}@{REDSHIFT_HOST}:{REDSHIFT_PORT}/{REDSHIFT_DBNAME}'
    redshift_table = 'city_weather'
    load_data_to_redshift(df, redshift_table, redshift_conn_str)

if __name__ == "__main__":
    main()