import requests
import pandas as pd
from sqlalchemy import create_engine

API_KEY = "VYWV7JS9JP6H5B36"
SYMBOL = "AAPL"

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={AAPL}&apikey={VYWV7JS9JP6H5B36}"

response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=VYWV7JS9JP6H5B36').json()

data = response['Time Series (Daily)']
df = pd.DataFrame(data).T
df.reset_index(inplace=True)

df.columns = ['date', 'open_price', 'high_price', 'low_price', 'close_price', 'volume']
df['symbol'] = SYMBOL
df['date'] = pd.to_datetime(df['date'])

print(df.head())

# SQL connection (MySQL)
engine = create_engine(
    "mysql+mysqlconnector://root:Rahul%4012@localhost:3306/stock_pipeline"
)

# Load into SQL
df.to_sql(
    name='stock_prices',
    con=engine,
    if_exists='append',
    index=False
)

print("✅ Data successfully loaded into SQL")
