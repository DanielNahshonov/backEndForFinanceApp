import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

API_KEY = os.getenv('STOCK_API_KEY')  # API-ключ для сервиса, например Alpha Vantage
BASE_URL = "https://www.alphavantage.co/query"  # Базовый URL API

def get_stock_data(symbol):
    """
    Получает данные о стоимости акций по символу (например, 'AAPL' для Apple).
    """
    params = {
        "function": "TIME_SERIES_INTRADAY",  # Тип данных, которые запрашиваем
        "symbol": symbol,  # Символ акции
        "interval": "5min",  # Интервал данных
        "apikey": API_KEY
    }

    try:
        # Создаем запрос, чтобы получить полный URL до выполнения
        request_url = requests.Request('GET', BASE_URL, params=params).prepare().url
        print(f"Request URL: {request_url}")  # Выводим полный URL

        # Отправляем запрос
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Проверка на ошибки
        data = response.json()

        if "Error Message" in data:
            raise ValueError(f"Error from API: {data['Error Message']}")

        return data

    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None
    
