import os
from flask import Flask
from flask_jwt_extended import JWTManager
from routes.auth import auth_bp
from routes.portfolio import portfolio_bp
from routes.stocks import stocks_bp
from flask_cors import CORS
from dotenv import load_dotenv
from db import init_db  # Импортируем функцию инициализации базы данных
from services.stock_service import get_stock_data  # Импортируем функцию для получения данных об акциях

load_dotenv()  # Загружаем переменные из .env файла

app = Flask(__name__)
CORS(app, origins="*")

# Загружаем конфигурацию
app.config.from_object('config.DevelopmentConfig')  # Используем конфигурацию для разработки
print("Config loaded:", app.config)  # Выводим конфигурацию

# Инициализация JWT
jwt = JWTManager(app)
print("JWT initialized")

# Подключение к базе данных MongoDB
db = init_db()  # Инициализация базы данных через функцию из db.py
print("Database 'financeApp' selected:", db)

# Регистрация маршрутов
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(portfolio_bp, url_prefix='/portfolio')
app.register_blueprint(stocks_bp, url_prefix='/stocks')

# Добавляем вызов функции для получения данных о акции AAPL при старте
stock_data = get_stock_data("AAPL")
print("Stock data for AAPL:", stock_data)  # Выводим полученные данные

print("Blueprints registered")

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True, host='0.0.0.0')