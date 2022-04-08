# Airflow Checkpoint Description

For this checkpoint we created an instance called “airflow2” in our Google Cloud Project: “crispy-computing-machine”... yes it is “2”, tests were made!

The instance runs an automated script (called airflow-setup.sh) provided in the Class lab, and modified for our files and project paths. This script installs Python 3, a virtual environment manager (venv) and Airflow.

The script is stored in one of our buckets (hint: look for the one which has ‘airflow’ and ‘start’ as keywords).

In order to access the Airflow Webserver the script creates a user with its corresponding password. The instance is modified with a firewall rule which opens port 8080 and whitelists certain IP addresses.