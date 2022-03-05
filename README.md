<div align="left"><img src="/images/ITAM.png"width="100" height="50">    <FONT SIZE=7>MCD</font></div>


<h2 align="left">crispy-computing-machine</h2>

# Project Proposal: Sentiment analysis in news and its impact in market indicators


## 1. Objectives

- What is the problem that your Data Product will solve?

We want to build a prediction model about cryptocurrency which can measure and predict market movements based on sentimental analysis extracted from journals and news.

- If a company was to use this application, what would be their ML objectives and business objectives?

The ML objective is to make accurate predictions about the cryptocurrency prices taking into main consideration the mechanisms of how news affects the market. The main business objective is to shed light to current and potential investors on how they could earn more money taking advantage of the insights in historic data.

## 2. Users

- Who will be the users of your application?

Current and potential investors. In short, people who are interested in make money :moneybag:

- How are users going to interact with your application?

Earlier iterations of our product will show predictions based on historical data, mainly doing assisted queries without any sophisticated UI. Advanced versions using our data product as inspiration could be deployed to users in dashboards using software such as Looker, Apache Superset or Mode.

## 3. Data Product Architecture Diagram 

![proposal-dag](https://user-images.githubusercontent.com/69408484/156854810-93d243af-cb5f-43cd-a804-1022436c2cbc.png)

## 4.Data

We will gather Data from two API´s:

 - [Coingecko](https://www.coingecko.com/)

 -  [NewsAPI](https://newsapi.org/)


We will be able to use the prices from the stock prices and the webpage´s news. Both API´s that will be used are free 

## 5. Modeling

The problem that our Data Product solves could be modeled as one of supervised learning   where the main output is the market price. However, this response variable could be modified to measure a change in the numeric value of a certain index or discretize it to only quantify changes in a certain range. An alternative could be to estimate whether it varies or not. In that case, the simplest model to estimate is a logistic regression and could also be implemented alternatively with a Random Forest classification model.

In any case, we would use pretrained models with implementations either in Python or R.

## 6. Evaluation

## 7. Inference

## 8. Compute

## 9. MVP

## 10. Pre-mortems

The availability of Data could be considered as the main problem 


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
