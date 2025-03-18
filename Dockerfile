# Используем Python 3.10 как базовый образ
FROM python:3.10

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем скрипт
COPY . .

# Устанавливаем переменные окружения для подключения к базе данных
ENV DB_HOST=db
ENV DB_USER=user
ENV DB_PASSWORD=password
ENV DB_NAME=testdb

# Запускаем скрипт
CMD ["sh", "-c", "python your_script.py & tail -f /dev/null"]
