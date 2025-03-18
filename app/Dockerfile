# Используем Python 3.10 как базовый образ
FROM python:3.10

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем скрипт
COPY . .

# Запускаем скрипт в бесконечном цикле
CMD ["sh", "-c", "while true; do python your_script.py; sleep 300; done"]