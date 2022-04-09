# Model description

In this folder you will find all the files related to the process of creating, tuning and deploying our Machine Learning model. The file `crypto_model_v1.ipynb` serves as the backbone of the entire process.

We represent our journey of this part of the project in the following diagram which we believe is useful to describe the different steps we took:

<div align="left"><img src="/images/training_model_diagram.png"width="1000" height="300">    <FONT SIZE=7></font></div>

## Data

The data we use for our model comes from the CoinGecko cryptocurrency API, which was introduced to our project as part of the ETL process described in the [src](https://github.com/kennyldc/crispy-computing-machine/tree/main/src) folder, and dumped into a GCP BigQuery dataset (we encourage you take a look to that folder if you have not already).

In order to start developing the model, we extracted the data from BigQuery, created a time column which helps us to represent our inputs in date format and we established a first type of hyperparameter (t0) to be modified and used as the initial day in model training. Every time we want to change the temporary cut-off point from which we will train the model, we will modify t0. Then we make sure with a summary that the data was imported correctly, visualizing if there were missing values and exploring the class types of each variable.

## Feature Engineering

The feature engineering part is contained in the `feature_engineering.py` file, which was also built from our backbone file. As you can see in the diagram, this sub-process serves as the entry gate for training the model in the form of a class. 

For the feature engineering work we used common modules as numpy and pandas but also created our own Python class objects (hats off to one of our team members which is a master). One particularly important object class was defined as “window_time” which is used to limit the range of dates for the analysis of currency prices (i.e. setting a time window from the data features).

In the `feature_engineering.py` file there is a broad well documentation of the code but in a basic description, the class: 1) defines the number of *backward* days from the specific t0 selected, 2) defines the number of *forward* days from the specific t0 selected, 3) specifies the number of days in which the data will be grouped, 4) extracts performance and metrics information from the ‘time window’ selected and 5) retrieves price movement from data (particularly registers if it went up or down). As intended, the code is flexible enough to define different dates and cryptocurrencies. 

An intermediate step is in the `transform.py` file which also works as an input for training the model. The code defines an object that helps to split the data in training and validation sets and has the option to scale certain features.

## Experiments 

Before choosing a model, we decided to elaborate more on some of the characteristics of the database, exploring in depth the characteristics of the variables, from their range and distribution, to their usefulness for the problem.`experiments.py` serves as evidence of this process. 

We consider this sub-process, as its name indicates, as a separate laboratory consisting of experiments where we were able to think better about building a machine learning tool to solve the problem. Our goal is to identify whether the price of the currency has gone up or down using the existing set of features. As part of the experiments we decided to work with a logistic regression, a random forest and a deep neural network.

## Algorithm

To solve our data problem we rely on one of the most powerful and popular algorithms in recent years: deep neural networks. Neural networks are focused on emulating the learning approach that humans use to gain certain types of knowledge. Like brain neurons, the method also contains a number of artificial ‘neurons’, and uses them to identify and store information. This network consists of input, hidden and output layers.  

The neurons take input data and simple operations are performed on those data. The results of these operations are passed to other neurons. Whether the result will be passed, is determined by the activation function. The activation function plays an important role for both feature extraction and classification.

While in the biological neural network, the size of dendrites varies in accordance with the importance of inputs. In the network, this is achieved by using weights and biases.

In the `train_v1.py` file, we develop all the training of our best model.

To do this, we start with the specification of certain values such as: the initial day (January 1, 2021), the number of days back to start the window (60), the number of days forward to make the prediction (7) and the percentage of price increase in the window (0.1).

For the network tuning, we specified a learning rate of 0.001, a batch size of 16, and ran 300 epochs for just the most popular currency in the base: BTC.

The trained network had an initial layer, 5 hidden layers, and an output layer. Each of the layers was decreasing in the number of perceptrons in multiples of 16. We combine between leakyReLU and Relu activations for the intermediate ones and determine a sigmoid activation for the output. After the second and third layer we proposed a dropout of 0.2. As optimizer we use "Adam" and as loss function "Binary Cross Entropy".


