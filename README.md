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

The key components of our data product architecture are displayed in Figure 1 to illustrate the interplay between system components. In a nutshell, Google Cloud Platform services guided the process and Python served as the main programming language.

![training_model_diagram drawio (1)](https://user-images.githubusercontent.com/69408484/168915229-34237da9-ca08-464b-a4af-1296abf07f29.png)

Finally, with all these decisions, we then construct our orchestration in Airflow in order to automate all the (re)training process. Our DAG’s make the same process described above with a daily execution at 06:00.

We strongly recommend to take a look: 

- At the [src](https://github.com/kennyldc/crispy-computing-machine/tree/main/src) folder for information about the data ingesting and feature engineering.

- At the [model](https://github.com/kennyldc/crispy-computing-machine/tree/main/model) folder for information about the model development and deployment.

- At the [Airflow](https://github.com/kennyldc/crispy-computing-machine/tree/main/Airflow) and [dags](https://github.com/kennyldc/crispy-computing-machine/tree/main/dags) folder for information about the Airflow orchestration.

## 4.Data :chart_with_upwards_trend:

The Data we use for our model comes from the [CoinGecko](https://www.coingecko.com/) cryptocurrency API that contains live prices, trading volume, exchange volume, trading pairs, historical data, contract address data, crypto categories, crypto derivatives, and images. We choose this API because it is free, reliable, and comprehensive.

From the API documentation, we obtained examples for our API Request Payloads. Because the API is free, our script does not need a key but it has a rate limit of 50 calls/minute. In practice we made a rate limit of 35 calls/minute using Python’s time.sleep() function so the API could not block us.

We extract historical data from the API making a request that lists all coins with id, name, and symbol. We performed a transformation intermediate process (that is why we identify our process as an ETL job) because we found numerous useless features from the API extraction such as the prices of the currencies in terms of another. After that, we write the data into Google Cloud Storage. 

Because one of our DAGs executes a extraction function, the data is always up to date.

## 5. Modeling :thought_balloon:

Our main objective by using ML is to predict if the price of a determined cryptocurrency goes up or goes down using historical data of the market capitalization, current price and market volume. 

Currently, we have a completed an end to end product for BTC using a deep neural network. We strongly recommend take a look at the [model](https://github.com/kennyldc/crispy-computing-machine/tree/main/model) folder for more information.

Deep neural networks are focused on emulating the learning approach that humans use to gain a certain type of knowledge. These neural networks learn hierarchical structures and levels of representation and abstraction to understand data patterns that come from various types of sources such as images, videos, sound, or text. The main idea behind an artificial neuron is quite simple. Has one or more inputs and one output. Depending on the value of those inputs, the neuron can be activated.  Like brain neurons, the method also contains a number of artificial ‘neurons’ and uses them to identify and store information. This network consists of input, hidden, and output layers. 

## 6. Evaluation :white_check_mark:

To evaluate the performance of our data product, we use purely technical metrics of machine learning, as well as tests that we carried out as a team in terms of usefulness. We also reflect whether the product satisfied the objectives set out in the definition of the problem and its limitations.

Our current deep network model for BTC achieves an accuracy of 0.8387. Let's remember that accuracy measures the percentage of cases in which the model has succeeded. Therefore we are in a good position with our specification. With our Binary Cross Entropy specification we achieved a loss of 0.6023. Finally, we obtained an AUC result of 0.7827. Overall, this standard machine learning evaluation metrics give evidence that the model is good enough.

As a team we also test our data product in terms of its usefulness. We put ourselves in the users' shoes and observed if the predictions made at a certain moment would work for us. Since the first prediction made with the BTC model was made more than a month ago and it was built for the probability of the next seven days, then we could go back to check if the prediction was good. The probability that the price would then rise by 10% for the next 7 days was as low as 15% and fortunately for our purposes (unfortunately for crypto users) the price did not go up. We became confident that the product accomplishes the goal of giving information to the users.

## 7. Inference :arrows_counterclockwise:

For the current version of our data product with BTC, we made predictions only once a day with a schelude DAG. Those predictions are stored into GCS and can be viewed using BigQuery.

We strongly recommend take a look at the [dags](https://github.com/kennyldc/crispy-computing-machine/tree/main/model) folder for more information.

Maybe with future iterations and more resources we could modifiy the inference process.

## 8. Compute :computer:

In the current version of our data product with BTC, only CPUs are required. The intesive part of training the models is made through VerteX AI services.

## 9. MVP :trophy:

For our MVP we want to complete a minimal useful workflow: extract historical data from the API and storage it in a Bucket, perform a basic EDA to visualize trends, execute queries inside BigQuery to get a glimpse of the data, make a basic feature engineering of the variables, test candidate ML models to make the prediction with logistic regressions inside BigQuery ML and neural networks inside Vertex AI if the price goes up or goes down, tune the hyperparameters and deploy the model to construct a web interface where our user could select a currency and a time window to see our prediction.

Tools from the GCP we’ll make our journey much easier! 

## 10. Pre-mortems :skull:

The number of currencies in our product multiplies the number of models and the potential pitfalls in our predictions.

Failures in the application comes more from the usability side of the users in the sense that we could provide inaccurate predictions. In terms of the engineering process, the complexity in the number of variables could interfere in the workflow. 

Another limitation is that this is a niche data product. Many common people could be completely unaffected by the crypto market and have no interest in it.
