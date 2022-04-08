<div align="left"><img src="/images/ITAM.png"width="100" height="50">    <FONT SIZE=7>MCD</font></div>


<h2 align="left">crispy-computing-machine</h2>

# Mastering crypto price movements with ML

# Members 

| **Name** |**email**|**ID**|**Github handler**| 
|:---:|:---:|:---:|:---:|
| Carlos Eduardo López de la Cerda Bazaldua | carlos.lopezdelacerda@itam.mx | 158122 | @kennyldc | 
| Miguel Ángel Reyes Retana | mreyesre@itam.mx | 045799 | @rrmiguel-2401 |
| Uriel Martínez Sánchez | umartin5@itam.mx | 000202942 | @urielmtzsa| 
| Peña Flores, Luis Fernando | luis.pena@itam.mx | 158488 | @TheKishimoto | 

**Miguel Reyes Retana**
- [Github profile ](https://github.com/rrmiguel-2401 "Miguel Reyes Retana")

**Carlos López de la Cerda**
- [Github profile ](https://github.com/kennyldc "Carlos López de la Cerda Bazaldua")

**Uriel Martínez Sánchez**
- [Github profile ](https://github.com/urielmtzsa "Uriel Martínez Sánchez")

**Peña Flores, Luis Fernando**
- [Github profile ](https://github.com/TheKishimoto "Peña Flores, Luis Fernando")

## Why we are the best team? :busts_in_silhouette:

We are the best team because we strongly believe that API stands for Amazing People Integrated... and we think that's beautiful.

## Repo structure 
    .
    ├── airflow                 # A description of the making of an Airflow setup inside a GCP Instance
    ├── dags                    # A folder where we'll describe our Airflow DAGs (currently empty)
    ├── model                   # A set of files which covers all the model process from training to production
    ├── src                     # Source files, API description and ETL process documentation
    ├── utils                   # An API token list which supplies information of the source data
    └── README.md

## Latest changes in our project :rotating_light:

### ML Model Trained Checkpoint :arrow_down_small:

Inside the `model` folder you will find the latest development with the training, execution, packaging and deployment of our model.

In more detail, in this last checkpoint we extracted the data from a BigQuery, did some feature engineering and feature selection adjustments to leave the most important information about cryptocurrencies and be able to train the model.

As part of the process of developing, we split our data into a training set and then applied a neural network to get the best currency price prediction for the most popular crypo: BTC. When put into operation with a validation test, the model obtained results as good as an accuracy of 0.894.

With this model as the winner, the next thing we did was to package it in a Docker container and adapt it to a production environment. In addition to this, the model was trained directly from Vertex AI (where it was also saved) and developed on an endpoint to also make predictions from there.

### Airflow Checkpoint :arrow_down_small:

Inside the `airflow` folder you will find a description of the process of creating an instance called “airflow2” in our Google Cloud Project... yes it is '2', tests were made!

The instance runs an automated script which installs Python 3, a virtual environment manager (venv) and Airflow. In order to access the Airflow Webserver the script creates a user with its corresponding password and has a firewall rule which opens port 8080 and whitelists certain IP addresses.

# Project description

## 1. ML and Business Objectives :muscle: :moneybag:

With more than 18,000 cryptocurrencies available in the market and 300 million users globally, information about these new trends are essential. Taking advantage of the movements in the future of the price of the coin you are investing will make you completely rich or completely poor in a second. 

Our team and our data product come to the aid to give new information to current and potential users in an unknown world and how to make better investing decisions and trade opportunities. 

We will build a prediction model with the current top six cryptocurrencies to measure if the price goes up or goes down in a specific time window.

## 2. Users :couple:

Users of our product are current and potential investors. In short, people who are interested in making money :moneybag:

Our data product will be displayed in a website. The user will be capable to select the currency of his/her interest and the number of days to make the prediction.

## 3. Data Product Architecture Diagram 

![diagram](https://user-images.githubusercontent.com/69408484/160226312-59a323a3-87e7-41a7-a803-0cf29ac04830.png)

## 4.Data :chart_with_upwards_trend:

[Coingecko](https://www.coingecko.com/) is a crypto API with data such as live prices, trading volume, exchange volumes, trading pairs, historical data, contract address data, crypto categories, crypto derivatives, images and more.

From API's documentation we obtained examples for our API Request Payloads. Even though the API does not require a key, it has a rate limit of 50 calls/minute, however, in practice we made a rate limit of 35 calls/minute so the API didn't block us.

In this first API Request Payload we get the top 6 market cap criptocurrencies from 01-01-2017 to 28-02-2022:

- btc
- eth
- bnb
- xrp
- luna
- sol

## 5. Modeling :thought_balloon:

Our model aims to predict if the price of a determined cryptocurrency goes up or goes down using historical data of the market capitalization, current price and market volume. 

In a second iteration of the modeling, potential variables such as facebook likes, twitter followers, reddit average posts, reddit average comments, reddit subscribers, reddit accounts active, developer data (forks, stars, subscribers, pull requests merged, pull request contributors, etc.) and public interest stats like alexa rank, could be explored to analyze if they have a relation with the price movements. 

In any case, the simplest model to estimate is a logistic regression and could also be implemented alternatively with a Random Forest classification model and neural networks.

We would use pretrained models with implementations in Python and BigQuery ML. 

## 6. Evaluation :white_check_mark:

To evaluate model performance we will rely on generic performance metrics such as accuracy, because we'll work on a classification ML problem (if the currency price goes up or goes down).

Success in our product could be measured by the monetary gains of our clients after a determined time. 

## 7. Inference :arrows_counterclockwise:

Our product consists in doing online prediction taking advantage of the low cost inside the GCP.

We wil only do inference when the user make the request for a specific currency in a specific period of time.

## 8. Compute :computer:

For the most part of our data product, devices with only CPU are enough while more sophisticated neural networks could use GPUs.

Only one device is enough and we are currently working in a VM with 2 vCPUs, 7.5 GB RAM, and TensorFlow 2.8 as the environment. We do not foresee having issues with billing. 

## 9. MVP :trophy:

For our MVP we want to complete a minimal useful workflow: extract historical data from the API and storage it in a Bucket, perform a basic EDA to visualize trends, execute queries inside BigQuery to get a glimpse of the data, make a basic feature engineering of the variables, test candidate ML models to make the prediction with logistic regressions inside BigQuery ML and neural networks inside Vertex AI if the price goes up or goes down, tune the hyperparameters and deploy the model to construct a web interface where our user could select a currency and a time window to see our prediction.

Tools from the GCP we’ll make our journey much easier! 

## 10. Pre-mortems :skull:

The number of currencies in our product multiplies the number of models and the potential pitfalls in our predictions.

Failures in the application comes more from the usability side of the users in the sense that we could provide inaccurate predictions. In terms of the engineering process, the complexity in the number of variables could interfere in the workflow. 

Another limitation is that this is a niche data product. Many common people could be completely unaffected by the crypto market and have no interest in it.

## 11. Next steps :feet:

While the MVP requires only information from the cryptocurrencies to make the prediction, other phenomena suchs a news and media impact could also be related to the price movements.In more advanced iterations we could explore these trends with new data sources.  

# Last modified:

Friday, April 8 by Uriel Martínez, Miguel Reyes and Carlos López de la Cerda.
