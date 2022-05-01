
import pickle
import pandas as pd
import numpy as np
from google.cloud import storage,aiplatform
from google.oauth2 import service_account

def predictions(bucket,X,Y,best,scaler,endpoint_name,features,predictions,auth):
    
    """
    Creates features and predictions csv files
    
    Parameters
    ----------        
    bucket : str
        Bucket name
    X : str
        Path from bucket of the object X
    Y : str
        Path from bucket of the object Y
    best : str
        Path from bucket of the list object best features
    scaler : str
        Path from bucket of the object scaler for the features
    endpoint_name : str
        Endpoint name
    features : str
        Path from bucket of the file features table
    predictions : str
        Path from bucket of the file predictions table
    auth: str
    	Path to google cloud credentials
        
    Returns
    -------
    str
        Predictions 
    """

    client = storage.Client.from_service_account_json(auth)
    gcs_bucket = client.get_bucket(bucket)

    blob = gcs_bucket.blob(X)
    with blob.open(mode = 'rb') as file:
        X = pickle.load(file)

    blob = gcs_bucket.blob(Y)
    with blob.open(mode = 'rb') as file:
        Y = pickle.load(file)

    blob = gcs_bucket.blob(best)
    with blob.open(mode = 'rb') as file:
        best=pickle.load(file)

    blob = gcs_bucket.blob(scaler)
    with blob.open(mode = 'rb') as file:
        scaler = pickle.load(file)

    df=X.merge(Y,how="outer",on=["symbol","ancla"])

    gcs_bucket.blob(features).upload_from_string(df.to_csv(index=False), 'csv')

    Xs=scaler.transform(X[best])
    
    credentials = service_account.Credentials.from_service_account_file(auth)
    aiplatform.init(credentials=credentials)
    
    endpoint = aiplatform.Endpoint(
        endpoint_name=aiplatform.Endpoint.list(filter=f'display_name="{endpoint_name}"')[0].resource_name
    )

    response = endpoint.predict([list(x) for x in Xs])

    Y_gorro=np.array(response[0])

    df["predict"]=Y_gorro

    df=df[["symbol","ancla","tgt","predict"]+best]

    gcs_bucket.blob(predictions).upload_from_string(df.to_csv(index=False), 'csv')

    return response
