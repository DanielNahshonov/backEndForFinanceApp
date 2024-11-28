import os
from flask import Flask
from flask_jwt_extended import JWTManager
from routes.auth import auth_bp
from routes.portfolio import portfolio_bp
from routes.stock import stock_bp
from flask_cors import CORS
from dotenv import load_dotenv
from db import init_db  # Импортируем функцию инициализации базы данных

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
app.register_blueprint(stock_bp, url_prefix='/stock')
print("Blueprints registered")

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)