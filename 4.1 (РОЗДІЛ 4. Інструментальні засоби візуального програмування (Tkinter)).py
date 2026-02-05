"""

Завдання 1. Написати програму, яка надсилає GET-запит до відкритого API та
виводить статус-код, заголовки і тіло відповіді. Додатково реалізувати POST-запит із
передачею даних.    

"""

import requests
import json

url_get = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response_get = requests.get(url_get)

    print(f"Статус-код: {response_get.status_code}")

    print("\nЗаголовки:")
    for key, value in response_get.headers.items():
        print(f"  {key}: {value}")

    print("\nТіло відповіді:")
    data_get = response_get.json()
    print(json.dumps(data_get, indent=4, ensure_ascii=False))

except requests.exceptions.RequestException as e:
    print(f"Помилка при GET-запиті: {e}")

print("\n" + "="*30 + "\n")
print("--- ВИКОНАННЯ POST-ЗАПИТУ ---")
url_post = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Мій тестовий заголовок",
    "body": "Це контент, відправлений через Python.",
    "userId": 1
}

try:
    response_post = requests.post(url_post, json=payload)

    print(f"Статус-код: {response_post.status_code}")
    
    print("\nВідповідь сервера (створений ресурс):")
    data_post = response_post.json()
    print(json.dumps(data_post, indent=4, ensure_ascii=False))

except requests.exceptions.RequestException as e:
    print(f"Помилка при POST-запиті: {e}")
