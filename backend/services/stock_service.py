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
    

def get_stock_news(keywords):
    """
    Получает новости о компании или рынке по ключевым словам.
    """
    params = {
        "function": "NEWS_SENTIMENT",
        "topics": keywords,
        "apikey": API_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Проверяем, есть ли новости
        if "feed" in data:
            return data["feed"]
        else:
            return []

    except Exception as e:
        print(f"Error fetching stock news: {e}")
        return None

def get_trending_news():
    """
    Получает трендовые рыночные новости.
    """
    params = {
        "function": "NEWS_SENTIMENT",  # Функция для получения новостей
        "apikey": API_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Проверяем, есть ли новости
        if "feed" in data:
            return data["feed"]
        else:
            return []

    except Exception as e:
        print(f"Error fetching trending news: {e}")
        return None