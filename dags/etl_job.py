
import json
import requests
import time
from datetime import timedelta,datetime
from google.cloud import bigquery,storage

def etl(date_request,bucket,crypto):
    
    """
    Gets data from CoinGecko API. Request is made from last day loaded in bucket + 1 to date_request
    
    Parameters
    ----------        
    date_request : date
        Last day for request
    bucket : str
        Bucket name
    crypto: list
        List of cryptos to make request
        
    Returns
    -------
    str
        If request was successful
    """
    
    base_url = 'https://api.coingecko.com/api/v3/'
    
    request=base_url+"coins/list"
    cat=requests.get(request).json()
    crypto_id=[]
    for i in crypto:
        crypto_id.append(next(item for item in cat if item["symbol"] == i)["id"])    
    
    client = bigquery.Client()
    query_job = client.query(
    """
    SELECT DISTINCT
        date
    FROM
        `crispy-computing-machine.crispy_dwh.crypto_btc`
    """)
    df = query_job.result().to_dataframe()
    date_start=max(df["date"].values)+timedelta(days=1)

    days=(date_request-date_start).days
    dates = [(date_start+timedelta(days=x)).strftime("%d-%m-%Y") for x in range(days+1)]
    
    if len(dates)>0:
        
        data=[]
        rate_minute_call=35

        i=0
        
        for cry in crypto_id:
            for dt in dates:
                i=i+1
                if (i % rate_minute_call)==1:
                    ahora=datetime.today()
                if (i % rate_minute_call)==0:
                    segundos=60-(datetime.today()-ahora).seconds
                    time.sleep(segundos) 
                request_body=base_url+f'coins/{cry}/history?date={dt}&localization=false'
                payload=requests.get(request_body).json()
                payload['date'] = dt
                payload['crypto'] = cry
                data.append(payload)  
        
        for row in data:
            try:
                row['market_data']['current_price']=row['market_data']['current_price']['usd']
                row['market_data']['market_cap']=row['market_data']['market_cap']['usd']
                row['market_data']['total_volume']=row['market_data']['total_volume']['usd']
            except:
                pass
            
        client = storage.Client()
        gcs_bucket = client.get_bucket(bucket)
        for row in data:
            path = f"crypto/{row['symbol']}/data_{row['date']}.json"
            blob = gcs_bucket.blob(path)
            with blob.open(mode = 'w') as file:
                json.dump(row, file)
                
        text='Successful request'
    
    else:
        
        text='The day entered is already loaded'
    
    return text
    
