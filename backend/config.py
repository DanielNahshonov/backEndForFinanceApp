import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env файла

class Config:
    MONGO_URI = os.getenv('MONGO_URI') 
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
    ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')  # API ключ для Alpha Vantage

class DevelopmentConfig(Config):
    """Конфигурация для разработки"""
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    """Конфигурация для продакшн"""
    DEBUG = False
    ENV = 'production'

class TestingConfig(Config):
    """Конфигурация для тестирования"""
    TESTING = True
    DEBUG = True
    ENV = 'testing'