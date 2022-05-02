# Project DAGs 

In this folder we show our Airflow DAGs scripts along with the Python files where the functions to execute each of the tasks are located and the SQL scripts to execute some views inside BigQuery.

## ETL DAG

Our first DAG is called **etl_dag** and is located in the `dag.py` file. This DAG has two tasks:

Task1 is a PythonOperator which calls a function that reads the crypto data files from the API and dumps them into a GCS bucket. 

The function is defined in the `etl_job.py` file and has two main arguments:

1) "date_request":  which is called using the Jinja Templating operator {{ yesterday_ds }}

2) "crypto":  in which we called from the dag a list specifying the top 6 cryptocurrencies: ['btc', 'eth', 'bnb', 'xrp', 'luna', 'sol', 'ada', 'avax', 'dot', 'doge'].

The rest of the arguments are designed to pass the name of the bucket and the GC credentials.

**The data generated is stored into a GCS bucket under the crypto folder.**

Task2 is a BigQuery view from the data stored in the first task. We show our SQL script (called `ddl.sql`) inside our SQL folder.

In the DAG we use BigQueryOperator, select some important features and drop them into a new table.

**The selection of the variables defined in the SQL script could be found under the SQL Workspace inside BigQuery.**

Task2 is dependent on Task1.

## MLOPs DAG

The second DAG designed for our project is called **training_dag** and is located in the `training_dag.py` file.

This DAG has five tasks: 

The first task is called Task0 (Python indexing… :stuck_out_tongue:) and it is defined as an ExternalTaskSensor which tracks the execution of the **etl_dag** (see above). Although this one is optional, we recommend including it in the process.

The following task (Task1) trains the model inside Vertex AI calling a Python function, **create_custom_job**, and put it in the DAG using a PythonOperator. 

The function is defined in the `jobs_train.py` file and is adapted from our model deployment more extensively described in the [Model folder](https://github.com/kennyldc/crispy-computing-machine/tree/main/model) from our Repo.

We highly recommend the reader take a look at that section for more details.

The main arguments specified in the **create_custom_job** are:

1) “date” : a date to execute the training job.

2) “display_name”: the name of the custom training job. 

3) “container_image_uri”: the image url of a docker container previously stored from the model process.

Complementary arguments define: the name of our GCP project, the GC credentials, a location for the region of the instance facilitated by Google, and an api_endpoint option for Job Service Client. Inside the DAG these values are extracted from the global variables inside Airflow (using Variable.get) and the parameters at the beginning of the code.

This function returns a response from where it executes the job in Vertex AI.

The next task (Task2) refers to the endpoint deployment and is also called from a Python function defined in the `endpoint.py` file. Related to the preceding task, in this process the function creates a model and deploys it into an endpoint using Vertex AI.

The function shares with the previous task the arguments of the date, the GC credentials, and a machine specification for the execution inside Vertex AI but also requires:

1) “name”: the name of the model in Vertex AI.

2) “model”: the bucket path of the model to deploy.

3) “image”: the container image uri.

After taking the values from the global variables and parameters the task completes the endpoint deployment.

The following task (Task3) creates features and predictions csv files using the information from the trained model in the preceding steps inside a Python function.

The “predictions” function is defined in the `predict_fp.py` file. There is also complementary information in the [Model folder](https://github.com/kennyldc/crispy-computing-machine/tree/main/model) from our Repo that is more or less required to fully understand the insides of the ML alternative proposed for the problem. However, for the purpose of defining what is inside of this function the most important arguments are: 

1) “X”: defined as the set of independent variables (mostly information about the price of the currency).

2) “Y”: the target variable (if the price will go up or down in a determined time)

3) “best”: an object that contains the best features available after running variable clustering in the feature selection process from the model specification.

4) “scaler”: an object that contains the scaler information (the process of standardizing the values to take values from 0 to 1) for the independent variables using minmaxscaler from scikit.learn.

5) “endpoint_name”: the name of the endpoint generated through Vertex AI.

Complementary arguments require the path to save the csv files and the GC credentials stored as variables. 

In the execution of this task, from the endpoint deployment of the model, the function calls a “predict” which ends up giving a probability (from 0 to 1) that the price of the currency goes up at a determined period of time.

All the information gets stored inside a GCS Bucket.

The last task (Task4) executes a SQL script (with a view) using BigQueryOperator in which we verify the accuracy of our predictions compared with the real movements of the crypto price. The script is found in the SQL/predicciones path of this folder.

In the table we can see number of the times that effectively the price goes up compared with the probability that our model has. The probability is incremental (by 0.1). Therefore, in the cases whith more probabibily from our model we expect seeing more times the price going up from our data.

Using the information from this table we stablish the cut-off point at 0.6 in which the 80% of the times we correctly predict that the price goes up. The lift is 4 times superior from the total of the sample.

From the MLOps Dag, all tasks are dependent on the previous.

# Dag and Instance schedule

Our DAGs are programmed to run at 6 AM daily. In order to save credits, our instance is scheduled to start daily at 5:50 and stop at 06:50. All hours correspond to Central UTC.

We provide the following evidence of the Instance schedule details:

<img width="1051" alt="Captura de Pantalla 2022-04-24 a la(s) 22 43 18" src="https://user-images.githubusercontent.com/69408484/165017296-c1f7d74b-12c9-485b-8629-96ad0170e8bf.png">

