"""Crispy DAG for ETL"""

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime
from airflow.utils.dates import days_ago
import os

import json
import requests
import time
from datetime import timedelta,datetime
from google.cloud import bigquery,storage

args = {
    'owner': 'Carlos Lopez',
    'email': 'caribaz@gmail.com',
    'retries': 3,
    'depends_on_past': True,
}

path = os.path.dirname(os.path.abspath(__file__))
sql_path = os.path.join(path, 'sql')
etl_path = os.path.join(sql_path, 'etl')
ddl_path = os.path.join(elt_path, 'ddl.sql')
ddl = open(ddl_path, mode='r').read()

params = {
    'folder': 'dags',
    'project_id': Variable.get("project_id")
}

dag = DAG(
    dag_id='etl_dag',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(0),
    tags=['bash', 'python', 'crispy', 'etl'],
    max_active_runs=1
)

task1 = BashOperator(
    dag=dag,
    task_id='update_dag',
    bash_command='sudo gsutil -m cp -r gs://params['bucket']/params['folder'] /home/airflow'
)

task2=PythonOperator(
    dag=dag,
    task_id='task4',
    python_callable=etl,
    op_kwargs={'date_request': '{{ yesterday_ds }}', 'bucket': Variable.get('crispy-bucket'), 'crypto': ['btc', 'eth', 'bnb', 'xrp', 'luna', 'sol', 'ada', 'avax', 'dot', 'doge'] }
)

task3 = BigQueryOperator(
    dag=dag,
    params=params,
    task_id = 'view_task',
    use_legacy_sql=False,
    sql=ddl
)

task1 >> task2 >> task3