"""Crispy DAG for ETL"""

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime
from airflow.utils.dates import days_ago
from crispy.etl_job import etl
import os

args = {
    'owner': 'Carlos Lopez',
    'email': 'caribaz@gmail.com',
    'retries': 3,
    'depends_on_past': True,
}

path = os.path.dirname(os.path.abspath(__file__))
sql_path = os.path.join(path, 'sql')
etl_path = os.path.join(sql_path, 'etl')
ddl_path = os.path.join(etl_path, 'ddl.sql')
ddl = open(ddl_path, mode='r').read()

params = {
    'bucket': Variable.get("bucket"),
    'folder': 'dags',
    'project_id': Variable.get("project-id")
}

dag = DAG(
    dag_id='etl_dag',
    default_args=args,
    schedule_interval='0 6 * * *',
    start_date=days_ago(0),
    tags=['bash', 'python', 'crispy', 'etl'],
    max_active_runs=1
)

task1 = BashOperator(
    dag=dag,
    params=params,
    task_id='update_dag_files',
    bash_command='sudo gsutil -m cp -r gs://{{ params.bucket }}/{{ params.folder }} /home/airflow'
)

task2=PythonOperator(
    dag=dag,
    task_id='run_etl_job',
    python_callable=etl,
    op_kwargs={'date_request': '{{ yesterday_ds }}', 'bucket': Variable.get('bucket'), 'crypto': ['btc', 'eth', 'bnb', 'xrp', 'luna', 'sol', 'ada', 'avax', 'dot', 'doge'], 'auth':Variable.get("auth")}
)


task1 >> task2
