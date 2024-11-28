from pymongo import MongoClient

# Модель для пользователя
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

# Модель для портфеля акций
class Portfolio:
    def __init__(self, email):
        self.email = email
        self.stocks = []