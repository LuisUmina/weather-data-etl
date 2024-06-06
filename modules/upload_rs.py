from sqlalchemy import create_engine, Table, Column, Integer, String, Float, MetaData
from sqlalchemy.dialects.postgresql import TIMESTAMP

def load_data_to_redshift(df, redshift_table, redshift_conn_str):
    engine = create_engine(redshift_conn_str)
    metadata = MetaData()
    
    table = Table(
        redshift_table, metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('country', String),
        Column('current_temp', Float),
        Column('feels_like', Float),
        Column('temp_min', Float),
        Column('temp_max', Float),
        Column('humidity', Integer),
        Column('wind_speed', Float),
        Column('cloudiness', Integer),
        Column('weather_main', String),
        Column('timestamp', TIMESTAMP)
    )

    metadata.create_all(engine)
    
    with engine.connect() as connection:
        for index, row in df.iterrows():
            insert_stmt = table.insert().values(
                id=row['id'],
                name=row['name'],
                country=row['country'],
                current_temp=row['current_temp'],
                feels_like=row['feels_like'],
                temp_min=row['temp_min'],
                temp_max=row['temp_max'],
                humidity=row['humidity'],
                wind_speed=row['wind_speed'],
                cloudiness=row['cloudiness'],
                weather_main=row['weather_main'],
                timestamp=row['timestamp']
            )
            connection.execute(insert_stmt)

    print(f"Datos cargados en la tabla {redshift_table}")