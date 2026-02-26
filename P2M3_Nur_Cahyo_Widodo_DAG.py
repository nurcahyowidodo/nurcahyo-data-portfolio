import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.empty import EmptyOperator
from elasticsearch import Elasticsearch
from elasticsearch import helpers

import psycopg2 as db

import pandas as pd

# function untuk ambil data dari postgresql
def fetch_postgre():
    conn = db.connect(
        database="postgres",
        user='airflow',
        password='airflow',
        host='postgres',
        port='5432')
    
    data = pd.read_sql('Select * from table_m3', con = conn)
    
    # save as csv
    data.to_csv('/opt/airflow/dags/P2M3_Nur_Cahyo_Widodo_data_raw.csv', index=False)

# function untuk read dan cleaning csv
def clean_data():
    df = pd.read_csv('/opt/airflow/dags/P2M3_Nur_Cahyo_Widodo_data_raw.csv')
    df = df.dropna()
    df = df.drop_duplicates()
    df.columns = (df.columns.str.strip().str.replace(' ', '_').str.lower())  
    df['invoicedate'] = pd.to_datetime(df['invoicedate'])
    
    df.to_csv('/opt/airflow/dags/P2M3_Nur_Cahyo_Widodo_data_clean.csv', index=False)

# upload data to elasticsearch
def load_elastic():
    # connect ke elastic
    es = Elasticsearch("http://elasticsearch:9200")
    df = pd.read_csv('/opt/airflow/dags/P2M3_Nur_Cahyo_Widodo_data_clean.csv')

    # ubah semua baris jadi list of dict
    records = df.to_dict(orient="records")

    # actions untuk bulk upload
    actions = []
    for doc in records:
        action = {
            "_index": "table_m3_cahyo",   
            "_source": doc       
        }
        actions.append(action)

    # bulk insert ke elastic
    response = helpers.bulk(es, actions)
    print(response)

default_args = {
    'owner': 'Cahyo',
    'start_date': dt.datetime(2020, 11, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
}


with DAG('DAG_CAHYO',
         default_args=default_args,
         schedule_interval='10,20,30 9 * 11 6',      # '0 * * * *',
         ) as dag:
    
    fetchPostgre = PythonOperator(task_id='fetch_postgre_data',
                                 python_callable=fetch_postgre)
    
    cleanData = PythonOperator(task_id='clean_data',
                                 python_callable=clean_data)
    
    uploadElastic = PythonOperator(task_id='upload_to_elastic',
                                 python_callable=load_elastic)

fetchPostgre >> cleanData >> uploadElastic 