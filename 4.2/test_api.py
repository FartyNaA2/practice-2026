import requests
import json

BASE_URL = "http://127.0.0.1:5000/users"

def print_response(response):
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    print("-" * 30)

print("1. ОТРИМАННЯ ВСІХ КОРИСТУВАЧІВ (GET)")
response = requests.get(BASE_URL)
print_response(response)

print("2. СТВОРЕННЯ НОВОГО КОРИСТУВАЧА (POST)")
new_user = {"name": "Іван", "role": "editor"}
response = requests.post(BASE_URL, json=new_user)
print_response(response)
created_id = response.json()["data"]["id"]

print(f"3. ОТРИМАННЯ КОРИСТУВАЧА {created_id} (GET)")
response = requests.get(f"{BASE_URL}/{created_id}")
print_response(response)

print(f"4. ОНОВЛЕННЯ КОРИСТУВАЧА {created_id} (PUT)")
update_data = {"name": "Іван Петрович", "role": "admin"}
response = requests.put(f"{BASE_URL}/{created_id}", json=update_data)
print_response(response)

print(f"5. ВИДАЛЕННЯ КОРИСТУВАЧА {created_id} (DELETE)")
response = requests.delete(f"{BASE_URL}/{created_id}")
print_response(response)

print("6. ПЕРЕВІРКА ПІСЛЯ ВИДАЛЕННЯ (GET)")
response = requests.get(BASE_URL)
print_response(response)
