import requests

BASE_URL = "http://127.0.0.1:5000"

print("--- 1. СПРОБА ДОСТУПУ БЕЗ ТОКЕНА ---")
response = requests.get(f"{BASE_URL}/profile")
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

print("\n--- 2. РЕЄСТРАЦІЯ ---")
user_data = {"username": "student", "password": "securePass123"}
requests.post(f"{BASE_URL}/register", json=user_data)
print("Користувача зареєстровано.")

print("\n--- 3. ЛОГІН (Отримання токена) ---")
auth_response = requests.post(f"{BASE_URL}/login", json=user_data)
if auth_response.status_code == 200:
    token = auth_response.json()['access_token']
    print(f"Токен отримано: {token[:20]}...")
else:
    print("Помилка входу")
    exit()

print("\n--- 4. ДОСТУП З ТОКЕНОМ ---")
headers = {'Authorization': f'Bearer {token}'}
profile_response = requests.get(f"{BASE_URL}/profile", headers=headers)
print(f"Status Code: {profile_response.status_code}")
print(f"Response: {profile_response.json()}")
