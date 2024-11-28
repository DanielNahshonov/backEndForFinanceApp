import requests
from config import ALPHA_VANTAGE_API_KEY

def get_stock_price(ticker):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    if 'Time Series (5min)' in data:
        latest_time = list(data['Time Series (5min)'].keys())[0]
        latest_price = data['Time Series (5min)'][latest_time]['4. close']
        return latest_price
    return None