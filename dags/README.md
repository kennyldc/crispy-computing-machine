# DAG chekpoint description

In this folder we provide the scripts of our Airflow DAG (dag.py) and the Python file which has the function to read the data from the crypto API and (after *several* and painful attempts) is dumped into a GCS bucket.

The DAG runs in the 'Airflow3' instance inside our project.

Our DAG has two tasks:

Task1 is a BashOperator which copies the dag file (from our dag folder inside GCS) to our VM. We find this task particularly helpful for debugging purposes. As you can imagine, instead of restarting the instance we just trigger a new DAG.

Task2 is a PythonOperator which calls a function that reads the crypto data files from the API and dumps them into a GCS bucket. The function has two important arguments: 1) "date_request" which is called using the Jinja Templating operator {{ yesterday_ds }} and 2) "crypto", in which we called from the dag a list specifying the top 6 cryptocurrencies: ['btc', 'eth', 'bnb', 'xrp', 'luna', 'sol', 'ada', 'avax', 'dot', 'doge'].

The data generated is stored into a GCS bucket under the crypto folder. 

Task2 is dependent on Task1.

We provide the following evidence of the successes and failures of our DAG:

<img width="306" alt="Captura de Pantalla 2022-04-24 a la(s) 20 16 02" src="https://user-images.githubusercontent.com/69408484/165005665-c3b923f1-7492-4c27-8258-8801d21518c2.png">

# Dag and Instance schedule

Our DAG is programmed to run at 6 AM daily. In order to save credits, our instance is scheduled to start daily at 5:50 and stop at 06:50. All hours correspond to Central UTC.

We provide the following evidence of the Instance schedule details:

<img width="1051" alt="Captura de Pantalla 2022-04-24 a la(s) 22 43 18" src="https://user-images.githubusercontent.com/69408484/165017296-c1f7d74b-12c9-485b-8629-96ad0170e8bf.png">

