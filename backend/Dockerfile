# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем весь код приложения в контейнер
COPY . .

# Устанавливаем переменную окружения для Flask
ENV FLASK_APP=app.py

# Указываем команду для запуска приложения
CMD ["flask", "run", "--host=0.0.0.0", "--port=$PORT"]