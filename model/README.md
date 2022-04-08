# Model description

In this folder you will find all the files related to the process of creating, tuning and deploying our Machine Learning model. The file `crypto_model_v1.ipynb` serves as the backbone of the entire process.

We represent our journey of this part of the project in the following diagram which we believe is useful to describe the different steps we took:

<div align="left"><img src="/images/training_model_diagram.png"width="1000" height="300">    <FONT SIZE=7></font></div>

## Data

The data we use for our model comes from the CoinGecko cryptocurrency API, which was introduced to our project as part of the ETL process described in the [src](https://github.com/kennyldc/crispy-computing-machine/tree/main/src) folder, and dumped into a GCP BigQuery dataset (we encourage you take a look to that folder if you have not already).

In order to start developing the model, we extracted the data from BigQuery, created a time column which helps us to represent our inputs in date format and we established a first type of hyperparameter (t0) to be modified and used as the initial day in model training. Every time we want to change the temporary cut-off point from which we will train the model, we will modify t0. Then we make sure with a summary that the data was imported correctly, visualizing if there were missing values and exploring the class types of each variable.
