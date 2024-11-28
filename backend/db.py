import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure  # Используем ConnectionFailure вместо ConnectionError

# Инициализация базы данных
def init_db():
    try:
        client = MongoClient(os.getenv('MONGO_URI'))
        db = client.get_database('financeApp')  # Указываем явно имя базы данных
        return db
    except ConnectionFailure as e:
        print(f"Error connecting to database: {str(e)}")
        raise e