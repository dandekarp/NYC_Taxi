import os

import pandas as pd


from sqlalchemy import create_engine
from time import time

import pyarrow.csv as pv
import pyarrow.parquet as pq 


def ingest_callable(user, password, host, port, db, table_name,parquet_name, csv_name):

    print(table_name,parquet_name)
    ##user = params.user
    ##password = params.password
    ##host = params.host
    ##port = params.port
    ##db = params.db
    ##table_name = params.table_name
    #parquet_name = 'input.parquet'
    #csv_name = 'output.csv'

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()

    print('connection established successfully, inserting data...')

    t_start = time()

    df = pd.read_parquet(parquet_name)
    df.to_csv(csv_name)
    ##df.drop("Unnamed: 0", axis=1, inplace=True)
    
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace') ##create table if doesn't exist

    df.to_sql(name=table_name, con=engine, if_exists='append')
    
    t_end = time()

    while True: 
        try:
            t_start = time()

            df = next(df_iter)
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
            df.to_sql(name=table_name, con=engine, if_exists='append')
            t_end = time()
            print('inserted another chunk, took %.3f second' % (t_end - t_start))
        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break
