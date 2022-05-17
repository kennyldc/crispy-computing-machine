## CoinGecko API

CoinGecko is a crypto API with data such as live prices, trading volume, exchange volumes, trading pairs, historical data, contract address data, crypto categories, crypto derivatives, images and more.

From [API's documentation](https://www.coingecko.com/en/api/documentation) we obtained examples for our API Request Payloads. Due to the API is free, our script doesn't need a key but it has a rate limit of 50 calls/minute, however, in practice we made a rate limit of 35 calls/minute in order to API didn't block us. To make it more automatizable, we used time.sleep() from Python  such that each 35 calls the code waits 60 seconds to continue with execution.

In this first API Request Payload we get the top 10 market cap criptocurrencies from 01-01-2021 to 28-02-2022:

- btc
- eth
- bnb
- xrp
- luna
- sol
- ada
- avax
- dot
- doge

**We are performing an ETL job** because we transform our payload before load in the bucket, specifically, we only keep with pair crypto/usd for current_price, market_cap, total_volume and discard other pairs crypto/crypyo (e.g. btc/eth).

We ran all the ETL job through a jupyter notebook instance of **Vertex AI** named *crispy-notebook-2022*. In such instance we cloned our GitHub repo with the purpose of use the ETL script and the YAML file. After get the data from the API, we storaged it into a **Google Cloud Storage** named *crispy-bucket-2022* with the following schema:

- crispy-bucket-2022/crypto/<<'crypto symbol'>>/data_dd-mm-yyyy.json 

Finally, we created a dataset in **Google BigQuery** named *crispy_dwh*, we created an **external table** named *crypto_btc* with all the data about Bitcoin in Google Cloud Storage, and we made one **view** from that table named *crypto_btc_view* in which we ordered the features that we think to use in the future for making predictions.  

## ETL brief summary

1. Define bucket name, cryptos (symbol) and time period from YAML file.
2. Load YAML variables.
3. Get id from crypto symbol through https://api.coingecko.com/api/v3/coins/list
4. Get API Request Payloads from https://api.coingecko.com/api/v3/coins/{cry}/history?date={dt}&localization=false
5. Add 'date' and 'crypto' items to payload json
6. Keep pair crypto/usd for current_price, market_cap, total_volume
7. Write into Google Cloud Storage

## First Exploratoy Data Analysis

When we made the API Request Payloads we noticed that payload gave us information about current price, market cap, volume, and features that we didn't expect such as facebook likes, twitter followers, reddit average posts, reddit average comments, reddit subscribers, reddit accounts active, developer data (forks, stars, subscribers, pull requests merged, pull request contributors, etc.) and public interest stats like alexa rank.
