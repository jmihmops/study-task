# Используем Python 3.10 как базовый образ
FROM python:3.10

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем скрипт
COPY . .

# Запускаем скрипт
CMD ["python", "your_script.py"]