-- DBeaver

DROP TABLE IF EXISTS luis_navia_2002_coderhouse.city_weather;

CREATE TABLE city_weather (
    id VARCHAR(50) NOT NULL,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(2) NOT NULL,
    current_temp DECIMAL(5, 2),
    feels_like DECIMAL(5, 2),
    temp_min DECIMAL(5, 2),
    temp_max DECIMAL(5, 2),
    humidity INTEGER,
    wind_speed DECIMAL(5, 2),
    wind_direction INTEGER,
    cloudiness INTEGER,
    weather_main VARCHAR(50),
    weather_description VARCHAR(100),
    timestamp TIMESTAMP NOT NULL
);