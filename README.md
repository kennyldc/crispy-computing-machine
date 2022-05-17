![Crispy Com](https://user-images.githubusercontent.com/69408484/168495208-69d62b90-8959-4581-9826-6ee32a3ec581.png)

# Mastering cryptocurrency price movements with Machine Learning

# Members 

| **Name** | **Email** | **ID** | **Github** | 
|:---:|:---:|:---:|:---:|
| Carlos Eduardo López de la Cerda Bazaldua | carlos.lopezdelacerda@itam.mx | 158122 | [@kennyldc](https://github.com/kennyldc) | 
| Miguel Ángel Reyes Retana | mreyesre@itam.mx | 45799 | [@rrmiguel-2401](https://github.com/rrmiguel-2401) |
| Uriel Martínez Sánchez | umartin5@itam.mx | 202942 | [@urielmtzsa](https://github.com/urielmtzsa) |


## Why we are the best team? :busts_in_silhouette:

We are the best team because we strongly believe that API stands for Amazing People Integrated... and we think that's beautiful.

## Repo structure 
    .
    ├── airflow                 # A description of how we created an Airflow setup inside a GCP instance
    ├── dags                    # The files and the description of our Airflow DAGs
    ├── model                   # A set of files and its decription which covers all the model process from training to production
    ├── src                     # Source files, API description and ETL process documentation
    ├── utils                   # An API token list which supplies information of the source data
    └── README.md

# Problem description 👀

With more than 18,000 cryptocurrencies available in the market and 300 million users globally, information about these new financial trends is essential. Taking advantage of the movements in the future of the price of the coin you are investing in will make you completely rich or completely poor in a second.

First introduced in 2008, Bitcoin has emerged as the main crypto in the market backed by a strong blockchain technology securing peer-to-peer transactions by cryptography. Nowadays the daily movements of BTC, as it is commonly abbreviated, are impressive. According to [Statista (2022)](https://www.statista.com/statistics/647374/worldwide-blockchain-wallet-users/), by the beginning of this year its daily trade volume was 31.11 billion US dollars with more than 270,000 user transactions. And while the exact number of owners is unknown, it is believed to be between [80](https://explodingtopics.com/blog/blockchain-stats#:~:text=Since%20its%20launch%20in%202009,than%2081%20million%20users%20worldwide) and [106](https://www.buybitcoinworldwide.com/how-many-bitcoin-users/) million. In particular, Bitcoin has been increasingly regarded as an investment asset and because of its highly volatile nature, our data product comes to the aid to give accurate predictions to guide investment decisions. 

In this project, we analyze the predictability of this market with enough flexibility to easily adapt our data architecture to more currencies. A ton of studies in the areas of finance, economics and statistics have put different machine learning models to compete to predict the price of Bitcoin, reaching the conclusion that the majority of this tools are good and useful enough to predict price changes in the short and long term. A particular example is that of Jaquart, Dann and Weinhart (2021), that showed that neural networks and gradient boosting classifiers have strong binary predictions but in a future span from 1 to 60 minutes.

With this in mind, if machine learning is good at predicting the price of bitcoin, why not improve it and build a flexible data architecture that could add more coins and more users? In this project we aim to solve this question by predicting with a deep neural network if the price of BTC goes up or goes down by a given probability and a specific number of days ahead set by the user.

## 2. Users :couple:

This application is designed for people who want to invest in cryptos and need accurate information to seize their money :moneybag:. We strongly believe that better information leads to better decisions and that this should be attainable for everyone, not only an elite or a small group of people. 

By this time our product is in the phase of model deployment and orchestration. However, in the future we would like to see it displayed in an aplication (either mobile or through a website). The user will be capable to select the currency of his/her interest and the number of days to make the prediction.

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
