"""Crispy DAG for ETL"""

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime
from airflow.utils.dates import days_ago
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
ddl_path = os.path.join(elt_path, 'ddl.sql')
ddl = open(ddl_path, mode='r').read()

params = {
    'bucket': Variable.get("bucket"),
    'folder': 'dags',
    'project_id': Variable.get("project_id")
}

dag = DAG(
    dag_id='etl_dag',
    default_args=args,
    schedule_interval='0 0 * * *',
    tags=['bash', 'python', 'crispy', 'etl'],
    max_active_runs=1
)

task1 = BashOperator(
    dag=dag,
    task_id='update_dag',
    bash_command='sudo gsutil -m cp -r gs://params['bucket']/dags /home/airflow'
)

task2 = PythonOperator(
    dag=dag,
    task_id='EL_task',
    python_callable=etl,
    op_kwargs={'date_request': , 'bucket': params['bucket'], 'crypto': btc}
)

task3 = BigQueryOperator(
    dag=dag,
    params=params,
    task_id = 'view_task',
    use_legacy_sql=False,
    sql=ddl
)

task1 >> task2 >> task3