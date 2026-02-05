import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DB_URL")
api_key = os.getenv("API_KEY")

if db_url and api_key:
    print(f"З'єднання з базою даних: {db_url}")
    print(f"Використання ключа API: {api_key}")
else:
    print("Помилка: Не вдалося завантажити змінні оточення.")
