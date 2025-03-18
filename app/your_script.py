import time
from datetime import datetime

if __name__ == "__main__":
    while True:
        # Выводим текущее время
        print(f"Current time: {datetime.now()}")
        # Задержка 5 минут
        time.sleep(300)