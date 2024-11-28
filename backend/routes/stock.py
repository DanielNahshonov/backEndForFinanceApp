from flask import Blueprint, jsonify

# Создаем Blueprint для маршрутов, связанных с акциями
stock_bp = Blueprint('stock', __name__)

# Пример маршрута, который возвращает список акций (фиктивные данные)
@stock_bp.route('/stocks', methods=['GET'])
def get_stocks():
    # Это просто пример. В реальной версии данные можно будет брать с внешнего API.
    stocks = [
        {"symbol": "AAPL", "name": "Apple", "price": 145.32},
        {"symbol": "GOOG", "name": "Google", "price": 2764.11},
        {"symbol": "AMZN", "name": "Amazon", "price": 3342.88}
    ]
    return jsonify(stocks), 200