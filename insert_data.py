"""
Quinn Cummings - 4/10/2021
-----------------------------------------------------
Effect:
extracts live data from the CoinLore API and loads data to 10 tables in MySql database on local linux system

"""



import requests
import json
from sqlalchemy import *
from datetime import datetime
from sqlalchemy.engine.url import URL


url = URL(drivername='mysql', username='quinn', password='xxxxxx', host='localhost', database='crypto')
engine = create_engine(url)
metadata = MetaData(engine)

bitcoin = Table('bitcoin', metadata,autoload=True, autoload_with=engine)
ethereum = Table('ethereum', metadata,autoload=True, autoload_with=engine)
binance_coin = Table('binance_coin', metadata,autoload=True, autoload_with=engine)
xrp = Table('xrp', metadata,autoload=True, autoload_with=engine)
polkadot = Table('polkadot', metadata,autoload=True, autoload_with=engine)
cardano= Table('cardano', metadata,autoload=True, autoload_with=engine)
litecoin = Table('litecoin', metadata,autoload=True, autoload_with=engine)
bitcoin_cash = Table('bitcoin_cash', metadata,autoload=True, autoload_with=engine)
stellar = Table('stellar', metadata,autoload=True, autoload_with=engine)
theta_token = Table('theta_token', metadata,autoload=True, autoload_with=engine)

btc_data ={}
eth_data ={}
binance_data ={}
xrp_data ={}
polka_data ={}
cardano_data ={}
lite_data ={}
btcCash_data ={}
stellar_data ={}
theta_data ={}
list_of_dicts = [[bitcoin,btc_data], [ethereum,eth_data], [binance_coin,binance_data], [xrp,xrp_data], [polkadot,polka_data], 
		[cardano,cardano_data], [litecoin,lite_data], [bitcoin_cash,btcCash_data], [stellar,stellar_data], [theta_token,theta_data]]
time = datetime.utcfromtimestamp(response['info']['time']).strftime('%Y-%m-%d %H:%M:%S')
	
response = requests.get("https://api.coinlore.net/api/tickers/")
response = json.loads(response.text)

def load_dict(dict_t):
    dict_t['price_usd'] = float(coin['price_usd'])
    dict_t['pct_change_24h'] = float(coin['percent_change_24h'])
    dict_t['time'] = str(time)
    dict_t['market_cap_usd'] = float(coin['market_cap_usd'])
    dict_t['coin_rank'] = int(coin['rank'])


for coin in response['data']:
  if coin['name'] in {'Bitcoin','Ethereum','Binance Coin','XRP','Polkadot','Cardano','Litecoin','Bitcoin Cash','Stellar','Theta Token'}:
    if coin['name'] == 'Bitcoin':
      load_dict(btc_data)

    elif coin['name'] == 'Ethereum':
      load_dict(eth_data)

    elif coin['name'] == 'Binance Coin':
      load_dict(binance_data)

    elif coin['name'] == 'XRP':
      load_dict(xrp_data)

    elif coin['name'] == 'Polkadot':
      load_dict(polka_data)

    elif coin['name'] == 'Cardano':
      load_dict(cardano_data)

    elif coin['name'] == 'Litecoin':
      load_dict(lite_data)

    elif coin['name'] == 'Bitcoin Cash':
      load_dict(btcCash_data)

    elif coin['name'] == 'Stellar':
      load_dict(stellar_data)

    elif coin['name'] == 'Theta Token':
      load_dict(theta_data)


def df_append(connection):
	for data in list_of_dicts:
		connection.execute(data[0].insert(), data[1])

with engine.begin() as conn:
    df_append(connection = conn)
