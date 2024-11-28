from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Portfolio
from pymongo import MongoClient

portfolio_bp = Blueprint('portfolio', __name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['stock_exchange']
portfolios_collection = db['portfolios']

@portfolio_bp.route('', methods=['POST'])
@jwt_required()
def create_portfolio():
    email = get_jwt_identity()
    data = request.get_json()
    ticker = data.get('ticker')
    quantity = data.get('quantity')

    portfolio = portfolios_collection.find_one({'email': email})
    if not portfolio:
        portfolio = {'email': email, 'stocks': []}

    portfolio['stocks'].append({'ticker': ticker, 'quantity': quantity})
    portfolios_collection.update_one({'email': email}, {'$set': portfolio}, upsert=True)

    return jsonify({'message': 'Stock added to portfolio'}), 200