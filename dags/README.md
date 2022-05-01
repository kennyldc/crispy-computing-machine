# Project DAGs 

In this folder we show our Airflow DAGs scripts along with the Python files where the functions to execute each of the tasks are located.

## ETL DAG

Our first DAG is called **etl_dag** and is located in the `dag.py` file. This DAG has two tasks:

Task1 is a PythonOperator which calls a function that reads the crypto data files from the API and dumps them into a GCS bucket. 

The function is defined in the `etl_job.py` file and has two main arguments:

1) "date_request":  which is called using the Jinja Templating operator {{ yesterday_ds }}

2) "crypto":  in which we called from the dag a list specifying the top 6 cryptocurrencies: ['btc', 'eth', 'bnb', 'xrp', 'luna', 'sol', 'ada', 'avax', 'dot', 'doge'].

The rest of the arguments are designed to pass the name of the bucket and the GC credentials.

**The data generated is stored into a GCS bucket under the crypto folder.**

Task2 is a BigQuery view from the data stored in the first task. Therefore, Task2 is dependent on Task1.

We provide the following evidence of the successes and failures of our DAG:

<img width="306" alt="Captura de Pantalla 2022-04-24 a la(s) 20 16 02" src="https://user-images.githubusercontent.com/69408484/165005665-c3b923f1-7492-4c27-8258-8801d21518c2.png">

# Dag and Instance schedule

Our DAG is programmed to run at 6 AM daily. In order to save credits, our instance is scheduled to start daily at 5:50 and stop at 06:50. All hours correspond to Central UTC.

We provide the following evidence of the Instance schedule details:

<img width="1051" alt="Captura de Pantalla 2022-04-24 a la(s) 22 43 18" src="https://user-images.githubusercontent.com/69408484/165017296-c1f7d74b-12c9-485b-8629-96ad0170e8bf.png">

