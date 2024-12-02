from flask import Blueprint, jsonify, request
from services.stock_service import get_stock_data

stocks_bp = Blueprint('stocks', __name__)

@stocks_bp.route('/<symbol>', methods=['GET'])
def fetch_stock_data(symbol):
    """
    Эндпоинт для получения данных об акции по символу.
    """
    print(f"Request received: {request.method} {request.url}")
    
    data = get_stock_data(symbol)

    if not data:
        return jsonify({'message': 'Failed to fetch stock data'}), 500

    return jsonify(data), 200

# @stocks_bp.route('/stocks/popular', methods=['GET'])
# def fetch_popular_stocks():
#     """
#     Эндпоинт для получения данных о популярных акциях.
#     """
#     data = get_popular_stocks()  # Предположим, эта функция возвращает список популярных акций.

#     if not data:
#         return jsonify({'message': 'No popular stocks found'}), 404

#     return jsonify({'stocks': data}), 200