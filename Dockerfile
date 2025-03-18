# Используем Python 3.10 как базовый образ
FROM python:3.10

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем скрипт
COPY your_script.py .

# Запускаем скрипт и записываем сообщение в лог
CMD ["/bin/sh", "-c", "echo 'Starting script at $(date)' && python your_script.py"]
RUN echo "shit shit shit"