# Model description

In this folder you will find all the files related to the process of creating, tuning and deploying our Machine Learning model. The file `crypto_model_v1.ipynb` serves as the backbone of the entire process.

We represent our journey of this part of the project in the following diagram which we believe is useful to describe the different steps we took:

<div align="left"><img src="/images/training_model_diagram.png"width="1000" height="300">    <FONT SIZE=7></font></div>

## Data

The data we use for our model comes from the CoinGecko cryptocurrency API, which was introduced to our project as part of the ETL process described in the [src](https://github.com/kennyldc/crispy-computing-machine/tree/main/src) folder, and dumped into a GCP BigQuery dataset (we encourage you take a look to that folder if you have not already).

In order to start developing the model, we extracted the data from BigQuery, created a time column which helps us to represent our inputs in date format and we established a first type of hyperparameter (t0) to be modified and used as the initial day in model training. Every time we want to change the temporary cut-off point from which we will train the model, we will modify t0. Then we make sure with a summary that the data was imported correctly, visualizing if there were missing values and exploring the class types of each variable.

For the following processs we will work only with the the most popular currency in the database: BTC.

## Feature Engineering

The feature engineering part is contained in the `feature_engineering.py` file, which was also built from our backbone file. As you can see in the diagram, this sub-process serves as the entry gate for training the model in the form of a class. 

For the feature engineering work we used common modules as numpy and pandas but also created our own Python class objects (hats off to one of our team members which is a master). One particularly important object class was defined as “window_time” which is used to limit the range of dates for the analysis of currency prices (i.e. setting a time window from the data features).

In the `feature_engineering.py` file there is a broad well documentation of the code but in a basic description, the class: 1) defines the number of *backward* days from the specific t0 selected, 2) defines the number of *forward* days from the specific t0 selected, 3) specifies the number of days in which the data will be grouped, 4) extracts performance and metrics information from the ‘time window’ selected and 5) retrieves price movement from data (particularly registers if it went up or down). As intended, the code is flexible enough to define different dates and cryptocurrencies. 

An intermediate step is in the `transform.py` file which also works as an input for training the model. The code defines an object that helps to split the data in training and validation sets and has the option to scale certain features.

## Experiments 

Before choosing a model, we decided to elaborate more on some of the characteristics of the database, exploring in depth the characteristics of the variables, from their range and distribution, to their usefulness for the problem.`experiments.ipynb` serves as evidence of this process. 

We consider this sub-process, as its name indicates, as a separate laboratory consisting of experiments where we were able to think better about building a machine learning tool to solve the problem. Our goal is to identify whether the price of the currency has gone up or down using the existing set of features. As part of the experiments we decided to work with a logistic regression, a random forest and a deep neural network.

## ML Metrics

With the logistic regression we obtained a score of .75. This is the probability for the user to obtain a predicted probability score of a given event using a logistic regression model. Random Forest gave us an accuracy of .98. This is not surprising. Random forests has been observed to overfit certain datasets with noisy classification tasks. The Deep Neural Network performed well and we feel we can still improve on the optimal configuration. 

## Algorithm

To solve our data problem we rely on one of the most powerful and popular algorithms in recent years: deep neural networks. Neural networks are focused on emulating the learning approach that humans use to gain certain types of knowledge. Like brain neurons, the method also contains a number of artificial ‘neurons’, and uses them to identify and store information. This network consists of input, hidden and output layers.  

The neurons take input data and simple operations are performed on those data. The results of these operations are passed to other neurons. Whether the result will be passed, is determined by the activation function. The activation function plays an important role for both feature extraction and classification.

While in the biological neural network, the size of dendrites varies in accordance with the importance of inputs. In the network, this is achieved by using weights and biases.

In the `train_v1.py` file, we develop all the training of our best model.

To do this, we start with the specification of certain values such as: the initial day (January 1, 2021), the number of days back to start the window (60), the number of days forward to make the prediction (7) and the percentage of price increase in the window (0.1).

For the network tuning, we specified a learning rate of 0.001, a batch size of 16, and ran 300 epochs for just the most popular currency in the base: BTC.

The trained network had an initial layer, 5 hidden layers, and an output layer. Each of the layers was decreasing in the number of perceptrons in multiples of 16. We combine between leakyReLU and Relu activations for the intermediate ones and determine a sigmoid activation for the output. After the second and third layer we proposed a dropout of 0.2. As optimizer we use "Adam" and as loss function "Binary Cross Entropy".

## Trade-offs

## Packaging 

Once we experimented and tested the ML model, we decided to go one step further. In this case, a particular focus of our team was to place special emphasis on the deployment of the work.

As a way to ensure the reproducibility of our work, we package the model in a Docker container. Within the same `crypto_model_v1.ipynb` file, there is the code section where we write a Dockerfile and save it.

Using the GCP tools we were able to create the container within the same cloud environment and deposit it in the Container Registry as an image. We provide the following evidence from our GCP project.

<img width="932" alt="Captura de Pantalla 2022-04-08 a la(s) 20 05 21" src="https://user-images.githubusercontent.com/69408484/162550638-fa5db7d0-8c69-4af3-a669-0594c78308c8.png">

## Training job using AI Training

In the `job_train.py` file, we create a function (called create_custom_job_sample) which simplifies the job of training the model using the AI Training tools inside the GCP. Our function requires: a) the name of our GCP project, b) the name of custom training job, c) the image url of the docker container, d) a location for the region of the instance facilitated by Google and e) an api_endpoint option for Job Service Client. 

This function returns a response from where it executes the job in Vertex AI.

## Model and endpoint deployment

As the penultimate part of our scheme, we focus on the model and endpoint deployment

In the `endpoint.py` file, we create a function (called model_endpoint) which creates a model through Vertex AI and deploys it into an endpoint from Vertex AI. Our function requires: a) the name of the model in Vertex AI, b) the bucket path of the model to deploy, c) the container image, and d) a machine type where the process will be executed. 

This function returns a response from where it executes the model and an endpoint in Vertex AI.

## Prediction from an End-Point :gem:

Finally we arrive at the last point of our ML journey!

Using all of the knowledge and tools from above we create our last code inside the `prediction.py` file.

Do you want to know the probability that the current price of the currency will rise by ‘P’ percent over the next ‘X’ days? We got you. 

Our last code predicts if the price from a selected day will go up a certain incremental rate “P” over the next “X” days. Our last function (called prediction) requires: a) the number of days back from the selected day, b) the number of days ahead “X” to make the prediction, c) the number of days grouped to get metrics in the observation window, d) the minimum percentage “P” increase to make the prediction, e) a list of selected features for the model, f) the bucket name where the model is stored, g) the endpoint name, and h) the day for the prediction (t0).

If the selected day (t0) is not in our database the code will print “The selected day is not yet available” otherwise it will start the magic! :crystal_ball:

The following is an example of the function executed from t0 = February 28th, 2022, with 60 days in the past, an expected increment of the current price by 10% (X = 0.1) for the next seven days (D = 7).

![Captura de Pantalla 2022-04-08 a la(s) 20 43 10](https://user-images.githubusercontent.com/69408484/162551842-661e6c16-a210-4c50-a988-dd42e50bd211.png)

We predict a 15.92% of probability that the price will go up. We expect our users to take this recomendation and make money!
