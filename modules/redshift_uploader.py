from sqlalchemy import create_engine, Table, Column, Integer, String, Float, MetaData
from sqlalchemy.dialects.postgresql import TIMESTAMP

def upload_to_redshift(df, redshift_table, redshift_conn_str):
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
    
    df.to_sql(redshift_table, engine, if_exists='replace', index=False)
    print(f"Data loaded into table {redshift_table} correctly")