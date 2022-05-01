
import datetime 
import pickle
import pandas as pd
from feature_engineering import window_time
from transform import scaler_split
from google.cloud import bigquery,storage,aiplatform

def predictions(vobs,vdes,step,incremental,best,bucket,scaler,endpoint_n,day):
    
    """
    Predicts if price from a selected day will go up certain incremental rate over 
    the next x days
    
    Parameters
    ----------        
    vobs : int
        Observation window backward for the selected day
    vdes : int
        Performance window forward for the selected day
    step: int
        Number of days grouped to get metrics in the observation window
    incremental : float
        Porcentage of increment minimum of the price in the performance window
    best : str
        Path from bucket of the list object best features
    bucket : str
        Bucket name
    scaler : str
        Path from bucket of the object scaler for the features
    endpoint_n : str
        Endpoint name
    day : datetime
        Day for the prediction
        
    Returns
    -------
    str
        Prediction for the selected day 
    """

    client = bigquery.Client()
    query_job = client.query(
    """
    SELECT DISTINCT
        date
    FROM
        `crispy-computing-machine.crispy_dwh.crypto_btc`
    """)
    df = query_job.result().to_dataframe()
    if day.date() not in df["date"].values:
        print("The selected day is not yet available")
        return 0
    else:
        query_job = client.query(
        """
        SELECT
            id
            ,symbol
            ,name
            ,date
            ,market_data.current_price as current_price
            ,market_data.market_cap as market_cap
            ,market_data.total_volume as total_volume  
        FROM
            `crispy-computing-machine.crispy_dwh.crypto_btc`
        """)
        df = query_job.result().to_dataframe()
        df["date"]=pd.to_datetime(df["date"])
        df=df[df["date"]>=day - datetime.timedelta(days = vobs)]
        df=df[df["date"]<=day + datetime.timedelta(days = vdes)]
        df.sort_values(by=["date"],ascending=True,inplace=True)
        df.reset_index(drop=True,inplace=True)
        df.reset_index(drop=False,inplace=True)
        df.rename(columns={"index":"t"},inplace=True)

        window=window_time(vobs=vobs,vdes=vdes,step=step,incremental=incremental)
        window.anclas(df['t'])
        window.anclai=df["t"].max()-window.vdes
        window.anclaf=df["t"].max()-window.vdes
        X=window.eng_X(df,['symbol','ancla'])
        
        client = storage.Client()
        gcs_bucket = client.get_bucket(bucket)
        blob = gcs_bucket.blob(best)
        with blob.open(mode = 'rb') as file:
            best=pickle.load(file)
        X=X[best]
        
        cp=df[df["t"]==df["t"].max()-window.vdes]["current_price"].values[0]

        blob = gcs_bucket.blob(scaler)
        with blob.open(mode = 'rb') as file:
            sc = pickle.load(file)
        X=sc.transform(X)

        endpoint = aiplatform.Endpoint(
        endpoint_name=aiplatform.Endpoint.list(filter=f'display_name="{endpoint_n}"')[0].resource_name)
        response = endpoint.predict([list(X[0])])
        
        print(f"Probability of current price ({round(cp,2)}) will go up {round(incremental*100,2)}% over the next {vdes} days is: {round(response.predictions[0][0]*100,2)}%")
        
        return response
