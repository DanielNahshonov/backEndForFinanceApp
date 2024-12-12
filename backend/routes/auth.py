import os
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from db import init_db  # Импортируем функцию инициализации базы данных

# Инициализация базы данных
db = init_db()
users_collection = db['users']

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register_user():
    print("Register function called")

    data = request.get_json()
    print("Received data:", data)

    email = data.get('email')
    password = data.get('password')

    # Проверка наличия email и пароля в запросе
    if not email or not password:
        print("Email or password missing")
        return jsonify({'message': 'Email and password are required'}), 400

    # Проверка, существует ли пользователь с таким email
    if users_collection.find_one({'email': email}):
        print(f"User with email {email} already exists")
        return jsonify({'message': 'User already exists'}), 400

    # Хеширование пароля
    hashed_password = generate_password_hash(password)
    print(f"Password hashed for {email}")

    try:
        result = users_collection.insert_one({'email': email, 'password': hashed_password})
        print(f"User created with ID: {result.inserted_id}")
    except Exception as e:
        print(f"Error during user creation: {str(e)}")
        return jsonify({'message': f'Error registering user: {str(e)}'}), 500

    print(f"User {email} registered successfully")
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Проверка наличия email и пароля в запросе
    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    # Поиск пользователя в базе данных
    user = users_collection.find_one({'email': email})
    if user and check_password_hash(user['password'], password):
        # Генерация JWT токена
        access_token = create_access_token(identity=email)
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/users', methods=['GET'])
def get_all_users():
    users = list(users_collection.find())
    for user in users:
        user['_id'] = str(user['_id'])  # Преобразуем ObjectId в строку
    return jsonify(users), 200