from flask import Blueprint, jsonify, request
from services.stock_service import get_stock_data , get_stock_news, get_trending_news

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

@stocks_bp.route('/news', methods=['GET'])
def fetch_stock_news():
    """
    Эндпоинт для получения новостей по ключевым словам.
    Пример: /stocks/news?keywords=TSLA
    """
    keywords = request.args.get('keywords', 'stock market')  # По умолчанию - общие новости
    print(f"Fetching news for keywords: {keywords}")

    news = get_stock_news(keywords)

    if not news:
        return jsonify({'message': 'No news found'}), 404

    return jsonify(news), 200


@stocks_bp.route('/news/trending', methods=['GET'])
def fetch_trending_news():
    """
    Эндпоинт для получения трендовых рыночных новостей.
    Пример: /stocks/news/trending
    """
    print("Fetching trending news...")

    news = get_trending_news()

    if not news:
        return jsonify({'message': 'No trending news found'}), 404

    return jsonify(news), 200