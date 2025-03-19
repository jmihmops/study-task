import os
import psycopg2

def main():
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_HOST'),
        port=os.getenv('POSTGRES_PORT')
    )
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    print(cursor.fetchone())
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()