import os
import psycopg2

# Получаем параметры подключения из переменных окружения
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

# Подключаемся к базе данных
conn = psycopg2.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    dbname=db_name
)
cursor = conn.cursor()

# Выполняем запрос
cursor.execute('SELECT version();')
db_version = cursor.fetchone()
print(f'Database version: {db_version}')

# Закрываем соединение
cursor.close()
conn.close()
