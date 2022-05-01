
# Necessary libraries

import pickle
import matplotlib.pyplot as plt
import datetime 
import numpy as np
import pandas as pd
from functools import reduce
from varclushi import VarClusHi
from google.cloud import aiplatform, bigquery, storage
from google.oauth2 import service_account
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import InputLayer, Dense, BatchNormalization, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l1_l2
from tensorflow.keras.losses import BinaryCrossentropy 
from tensorflow.keras.callbacks import ModelCheckpoint,EarlyStopping
from feature_engineering import window_time
from transform import scaler_split

# Variables model

# Data engineering
t0 = datetime.datetime(2021, 1, 1) # Initial day
vobs=60 # Observation window backward for each day
vdes=7 # Performance window forward for each day
step=15 # Numer of days grouped to get metrics in the observation window
incremental=0.1 # Porcentage of increment minimum of the price in the performance window 

# Scaler and Split
val=0.1 # Validation set size
test=0.1 # Test set size
r_s=220327 # Random state
scaler='MinMaxScaler' # Escalation method

# Model
lr = 0.0001 # learning rate
bs = 16 # batch size
e = 300 # epochs

# Bucket
BUCKET = 'crispy-bucket-2022'
coin = 'btc'
version = 'v1'

# Get data from Big Query

#client = bigquery.Client()
credentials = service_account.Credentials.from_service_account_file("/.auth/crispy-key-2022.json", scopes=["https://www.googleapis.com/auth/cloud-platform"])
client = bigquery.Client(credentials=credentials, project=credentials.project_id)
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
df=df[df["date"]>=t0]
df.sort_values(by=["date"],ascending=True,inplace=True)
df.reset_index(drop=True,inplace=True)
df.reset_index(drop=False,inplace=True)
df.rename(columns={"index":"t"},inplace=True)

# Feature Engineering 

window=window_time(vobs=vobs,vdes=vdes,step=step,incremental=incremental)
window.anclas(df['t'])
X=window.eng_X(df,['symbol','ancla'])
Y=window.eng_Y(df)

client = storage.Client()
gcs_bucket = client.get_bucket(BUCKET)

blob = gcs_bucket.blob(f'models/{coin}/{version}/X_{version}.pkl')
with blob.open(mode = 'wb') as file:
    pickle.dump(X,file)
    
blob = gcs_bucket.blob(f'models/{coin}/{version}/Y_{version}.pkl')
with blob.open(mode = 'wb') as file:
    pickle.dump(Y,file)

# Features selection

um=['symbol','ancla']
varc = sorted(X.filter(like='x_').columns)
vart = ['tgt']

# Outliers

for v,li,ls in X[varc].describe(percentiles=[0.01,0.99]).T[['1%','99%']].reset_index().values:
    X[f'ex_{v}'] = ((X[v]<li)|(X[v]>ls)).astype(int)   
X['ex_'] = X.filter(like= 'ex_').max(axis=1)
X = X.loc[X['ex_']==0].reset_index(drop=True)
X.drop(X.filter(like='ex_').columns,axis=1,inplace=True)

# Multicollinearity

vc = VarClusHi(df=X,feat_list=varc)
vc.varclus()
rs = vc.rsquare
rs = rs.sort_values(by=['Cluster','RS_Ratio']).reset_index(drop=True)
rs['id'] = rs.groupby('Cluster').cumcount()+1
best = rs.loc[rs['id']==1]['Variable'].tolist()

blob = gcs_bucket.blob(f'models/{coin}/{version}/best_{version}.pkl')
with blob.open(mode = 'wb') as file:
    pickle.dump(best,file)

# Scaler and Split

tad = X[um+best].merge(Y,on=um,how='left')
sp=scaler_split(df=tad,X=best,Y=vart)
sp.split(val=val,test=test,rs=r_s)
sc = sp.scaler(scaler)

blob = gcs_bucket.blob(f'models/{coin}/{version}/scaler_{version}.pkl')
with blob.open(mode = 'wb') as file:
    pickle.dump(sc,file)
    
# Build model

checkpoints = ModelCheckpoint("model.h5",monitor='val_loss',verbose=10,save_best_only=True,
                              save_weights_only=False,mode="min",save_freq='epoch')
early_stop = EarlyStopping(monitor='val_loss', patience=10)

DNN = Sequential()
DNN.add(InputLayer(input_shape=sp.X_train.shape[1]))
DNN.add(Dense(2048, activation='relu'))
DNN.add(Dropout(rate=0.2))
DNN.add(Dense(1024, activation='relu',kernel_regularizer = l1_l2(0.001, 0.001)))
DNN.add(Dropout(rate=0.2))
DNN.add(Dense(256, activation='relu'))
DNN.add(BatchNormalization())
DNN.add(Dense(64, activation='relu'))
DNN.add(Dense(16, activation='relu',kernel_regularizer = l1_l2(0.01, 0.01)))
DNN.add(Dense(units=sp.Y_train.shape[1], activation='sigmoid'))
DNN.compile(optimizer=Adam(lr), loss= BinaryCrossentropy(),metrics=['accuracy','AUC'])
DNN.fit(x=sp.X_train, y=sp.Y_train, batch_size=bs, epochs=e, validation_data=(sp.X_val, sp.Y_val),callbacks=[checkpoints,early_stop])
model = load_model("model.h5")
model.save('gs://' + BUCKET + f'/models/{coin}/{version}/model_{version}')
