# Weather Data ETL Project

This project is an ETL (Extract, Transform, Load) tool that extracts data from the OpenWeatherM API, transforms it, and loads it into an Amazon Redshift database.

## Project Structure
- `__main__.py`: Main file that coordinates the execution of the ETL flow.
- `parameters.py`: Contains basic parameters and configurations such as the base URL of the API.
- `modules/`:
  - `__init__.py`: Initializes the modules.
  - `api_data_extraction.py`: Contains the `get_weather_data` function that extracts data from the API.
  - `data_processing.py`: Contains the `process_weather_data` function that transforms the extracted data.
  - `redshift_uploader.py`: Contains the `upload_to_redshift` function that loads the transformed data into Amazon Redshift.
- `sql/`:
  - `create_table.sql`: SQL file to create the `city_weather` table in Redshift (executed via DBeaver).
- `.env`: Configuration file that contains the API keys and Redshift credentials (provided through the CODERHOUSE platform).

## Configuration

- **Environment Variables**:
The values were provided through the CODERHOUSE platform. Update the `.env` file in the project root with the following content:
```plaintext
OPENWEATHERMAP_API_KEY='api_key'
REDSHIFT_USERNAME='usuario_redshift'
REDSHIFT_PASSWORD='contraseña_redshift'
REDSHIFT_HOST='host_redshift'
REDSHIFT_PORT='puerto_redshift'
REDSHIFT_DBNAME='tbase_de_datos_redshift'
