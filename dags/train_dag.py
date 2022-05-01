"""Training DAG for crypto BTC"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.models import Variable
from datetime import datetime
from airflow.utils.dates import days_ago
from crispy.jobs_train import create_custom_job
from crispy.endpoint import model_endpoint
from crispy.predict_fp import predictions

args = {
    'owner': 'Uriel Martinez',
    'email': 'uriel.mtzsa@gmail.com',
    'retries': 2,
    'depends_on_past': True,
}

params = {
    'container': 'gcr.io/crispy-computing-machine/model@sha256:42c5b70a88ef4ae57bab8d5d6ba9e0afe7a1b5ae5a5e0c8f1b3b4688ab6cb9dd',	
    'image' : 'gcr.io/cloud-aiplatform/prediction/tf2-cpu.2-3:latest',
    'machine': 'n1-standard-4'
}

dag = DAG(
    dag_id='training_dag',
    default_args=args,
    #schedule_interval='* * * * *',
    #start_date=datetime(2022, 4, 30),
    schedule_interval='0 6 * * *',
    start_date=days_ago(0),
    catchup=True,
    tags=['python', 'crispy', 'train'],
    max_active_runs=1
)

task0 = ExternalTaskSensor(
    dag=dag,
    task_id='etl_task_sensor',
    external_dag_id='etl_dag',
    external_task_id='run_etl_job'
)


# Task 1: Train model
task1=PythonOperator(
    dag=dag,
    params=params,
    task_id='vertex_ai_training',
    python_callable=create_custom_job,
    op_kwargs={'date': '{{ ds }}', 'project': Variable.get('project-id'), 'display_name': 'model_v1', 'container_image_uri':'{{ params.container }}','auth':Variable.get("auth"),'location': 'us-central1', 'api_endpoint' : 'us-central1-aiplatform.googleapis.com'}
)

# Task 2: Endpoint Deployment
task2=PythonOperator(
    dag=dag,
    params=params,
    task_id='endpoint_deployment',
    python_callable=model_endpoint,
    op_kwargs={'date': '{{ ds }}', 'name': 'model_v1', 'model': Variable.get('model'), 'image': '{{ params.image }}','auth': Variable.get("auth"),'machine' : '{{ params.machine }}'}
)

# Task 3: Update features and predictions tables
task3=PythonOperator(
    dag=dag,
    task_id='features_predictions',
    python_callable=predictions,
    op_kwargs={'bucket': Variable.get('bucket'), 'X': 'models/btc/v1/X_v1.pkl','Y': 'models/btc/v1/Y_v1.pkl','best': 'models/btc/v1/best_v1.pkl','scaler': 'models/btc/v1/scaler_v1.pkl','endpoint_name': "model_v1_{{ ds }}_endpoint",'features': 'models/btc/v1/features_v1.csv','predictions': 'models/btc/v1/predictions_v1.csv','auth': Variable.get("auth") }
)

#task3
#task1 >> task2 >> task3
task0 >> task1 >> task2 >> task3
