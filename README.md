<div align="left"><img src="/images/ITAM.png"width="100" height="50">    <FONT SIZE=7>MCD</font></div>


<h2 align="left">crispy-computing-machine</h2>

# Project Proposal Title: Mastering crypto price movements with ML


## 1. Objectives

- What is the problem that your Data Product will solve?

We want to build a prediction model about cryptocurrency which can measure and predict market movements based on sentiment analysis extracted from journals and news.

- If a company was to use this application, what would be their ML objectives and business objectives?

The ML objective is to make accurate predictions about the cryptocurrency prices taking into consideration the mechanisms of how news affects the market. The main business objective is to shed light to current and potential investors on how they could earn more money taking advantage of the insights in historic data.

## 2. Users

- Who will be the users of your application?

Current and potential investors. In short, people who are interested in making money :moneybag:

- How are users going to interact with your application?

Earlier iterations of our product will show predictions based on historical data, mainly doing assisted queries without any sophisticated UI. Advanced versions using our data product as inspiration could be deployed to users in dashboards using software such as Looker or Mode.

## 3. Data Product Architecture Diagram 

![proposal-dag](https://user-images.githubusercontent.com/69408484/156854810-93d243af-cb5f-43cd-a804-1022436c2cbc.png)

## 4.Data

We will gather Data from two API´s:

 - [Coingecko](https://www.coingecko.com/)

 -  [NewsAPI](https://newsapi.org/)


We will be able to use the prices from the currencies and the webpage´s news. Both API´s that will be used are free.

## 5. Modeling

The problem that our Data Product solves could be modeled as one of supervised learning where the main output is the market price and one of the inputs consist of some sort of metric about the sentiment in news media. However, this response variable could be modified to measure a change in the numeric value of a certain index or discretize it to only quantify changes in a certain range. An alternative could be to estimate whether it varies or not. In that case, the simplest model to estimate is a logistic regression and could also be implemented alternatively with a Random Forest classification model.

One of the main features of our project is that our main input, the sentiment analysis in news, requires at the same time some kind of modeling effort where the titles and the corpus of the articles are processed to indicate whether it has positive or negative characteristics about the cryptocurrency in the data. In this case, natural language processing models come in handy.

In any case, we would use pretrained models with implementations either in Python or R.

## 6. Evaluation

- How would you evaluate your model performance, both during training and inference?

To evaluate model performance we will rely on generic performance metrics such as accuracy.

- How would you evaluate whether your application satisfies its objectives?

For our first iterations evaluations will consist mostly on performance inside the model. In a real case scenario, success in our product could be measured by the monetary gains of our clients after a determined time. 

## 7. Inference

- Will you be doing online prediction or batch prediction or a combination of both?

Our product consists in doing online prediction due to the necessity of timely actualizations everytime an article is published. It also has advantages such as low cost inside the GCP. See also  -  [Online vs Batch prediction](https://cloud.google.com/ai-platform/prediction/docs/online-vs-batch-prediction)

- Can you run inference on CPUs or an edge device or do you need GPUs?

For the most part of our MVP, devices with only CPU are enough. More sophisticated iterations and models, particularly in the natural language processing side, could use devices with GPU.

## 8. Compute

Same as with inference, for the most part of our MVP devices with only CPU are enough. More sophisticated iterations and models, particularly in the natural language processing side, could use devices with GPU.

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
