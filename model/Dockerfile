
FROM gcr.io/deeplearning-platform-release/tf2-cpu.2-3

RUN pip install varclushi

WORKDIR /

RUN mkdir /.auth
COPY crispy-key-2022.json /.auth/crispy-key-2022.json
COPY feature_engineering.py /feature_engineering.py
COPY transform.py /transform.py
COPY train_v1.py /train_v1.py

CMD export GOOGLE_APPLICATION_CREDENTIALS="/.auth/crispy-key-2022.json"
CMD gcloud auth activate-service-account 421888395673-compute@developer.gserviceaccount.com --key-file=/.auth/crispy-key-2022.json --project=crispy-computing-machine
CMD gcloud config set account 421888395673-compute@developer.gserviceaccount.com
CMD gcloud config set project crispy-computing-machine

ENTRYPOINT ["python", "-m", "train_v1"]
