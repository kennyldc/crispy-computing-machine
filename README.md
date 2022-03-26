<div align="left"><img src="/images/ITAM.png"width="100" height="50">    <FONT SIZE=7>MCD</font></div>


<h2 align="left">crispy-computing-machine</h2>

# Project Proposal Title: Mastering crypto price movements with ML


## 1. ML and Business Objectives :muscle: :moneybag:

- What is the problem that your Data Product will solve?

With more than 18,000 cryptocurrencies available in the market and 300 million users globally, information about these new trends are essential. Taking advantage of the movements in the future of the price of the coin you are investing will make you completely rich or completely poor in a second. 

Our team and our data product come to the aid to give new information to current and potential users in an unknown world and how to make better investing decisions and trade opportunities. 

We will build a prediction model with the current top six cryptocurrencies to measure if the price goes up or goes down in a specific time window.

## 2. Users :couple:

- Who will be the users of your application?

Current and potential investors. In short, people who are interested in making money :moneybag:

- How are users going to interact with your application?

Our data product will be displayed in a website. The user will be capable to select the currency of his/her interest and the number of days to make the prediction.

## 3. Data Product Architecture Diagram 

![proposal-dag](https://user-images.githubusercontent.com/69408484/156854810-93d243af-cb5f-43cd-a804-1022436c2cbc.png)

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

## 9. MVP

- What would the MVP be?

A simple MVP would be capable of presenting a summary of the number of news related to our crypto in a certain period of time, indicate whether they were positive or negative and show how this could affect the price. The user will have the ability of changing certain parameters such as the historical period for news to get analyzed and characteristics of the media source.

Additional layers of complexity could be added tuning the NLP algorithms, the prediction ML models and the user interface.

- How difficult is it to get there?

We need to gather data from two different sources and understand two different API documentations. It is also difficult to find the best models for sentiment analysis and the ML tools to get a reasonable prediction. A decent output interface could also be problematic taking into consideration the different profiles of users.

## 10. Pre-mortems

- What are the risky aspects of the project? 

There is a possibility of a mismatch between the news articles and the currencies we want to include in our product. For example, many articles related to Bitcoin but almost zero for Ethereum. It is also possible that even though we are still in ways to explore certain connections between the two sources of information, it turns out that they are completely unrelated.
Less dramatic failures could be in terms of poor performance models.

- If your team fails to build the application you want, what do you think might have caused the failure?

It could be the mismatch and no correlation of the two sources or a problem in the data we are including. For example, low coverage of media from all parts of the world.

- What are the limitations of your application?

This is a niche data product. Many common people could be completely unaffected by the crypto market and have none interest in it. 

- What are the potential biases of your application?

We could be manipulating the relation between news and the crypto market and falling into the trap of establishing causality in a correlation scenario.

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

We are the best team because we strongly believe that API stands for Amazing People Integrated... and we think that's beautiful. 
