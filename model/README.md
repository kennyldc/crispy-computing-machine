# Model description

In this folder you will find all the files related to the process of creating, tuning and deploying our Machine Learning model. The file `crypto_model_v1.ipynb` serves as the backbone of the entire process.

We represent our journey of this part of the project in the following diagram which we believe is useful to describe the different steps we took:

<div align="left"><img src="/images/training_model_diagram.png"width="1000" height="300">    <FONT SIZE=7></font></div>

## Data

The data we use for our model comes from the CoinGecko cryptocurrency API, which was introduced to our project as part of the ETL process described in the [src](https://github.com/kennyldc/crispy-computing-machine/tree/main/src) folder, and dumped into a GCP BigQuery dataset (we encourage you take a look to that folder if you have not already).

In order to start developing the model, we extracted the data from BigQuery, created a time column which helps us to represent our inputs in date format and we established a first type of hyperparameter (t0) to be modified and used as the initial day in model training. Every time we want to change the temporary cut-off point from which we will train the model, we will modify t0. Then we make sure with a summary that the data was imported correctly, visualizing if there were missing values and exploring the class types of each variable.

## Feature Engineering

The feature engineering part is contained in the `feature_engineering.py` file, which was also built from our backbone file. As you can see in the diagram, this sub-process serves as the entry gate for training the model in the form of a class. 

For the feature engineering work we used common modules as numpy and pandas but also created our own Python class objects (hand down to one of our team members which is a master). One particularly important object class was defined as “window_time” which is used to limit the range of dates for the analysis of currency prices (i.e. setting a time window from the data features).

In the `feature_engineering.py` file there is a broad well documentation of the code but in a basic description, the class: 1) defines the number of *backward* days from the specific t0 selected, 2) defines the number of *forward* days from the specific t0 selected, 3) specifies the number of days in which the data will be grouped, 4) extracts performance and metrics information from the ‘time window’ selected and 5) retrieves price movement from data (particularly registers if it went up or down). As intended, the code is flexible enough to define different dates and cryptocurrencies. 
