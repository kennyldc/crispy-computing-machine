# Airflow Checkpoint Description

For this checkpoint we created an instance that runs an automated script (called airflow-setup.sh) provided in the Class lab, and modified for our files and project paths. This script installs Python 3, a virtual environment manager (venv) and Airflow.

The script is stored in one of our buckets.

In order to access the Airflow Webserver the script creates a user with its corresponding password. The instance is modified with a firewall rule which opens port 8080 and whitelists certain IP addresses.

# We provide the following images as evidences of our Airflow setup

## Airflow log in:

![airflow1](https://user-images.githubusercontent.com/69408484/162349582-97df0d98-fdf4-4a68-8e82-4702beee578f.jpeg)

## Navigating inside DAGS section in Airflow:

![airflow2](https://user-images.githubusercontent.com/69408484/162349729-1d10c2f8-30b2-4810-a73c-39f250a63154.jpeg)

## User information evidence: 

![airflow3](https://user-images.githubusercontent.com/69408484/162349832-c71262fc-d4ef-4140-8391-dee8289c6c99.jpeg)

## Editing connection information:

![airflow4](https://user-images.githubusercontent.com/69408484/162349895-296f4fd5-90aa-4770-9498-3da22e58f992.jpeg)
