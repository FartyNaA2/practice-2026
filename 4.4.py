"""

Завдання 4. Написати програму, що обчислює геш рядка за алгоритмом SHA-256,
виконує шифрування і розшифрування повідомлення симетричним методом (AES), а
також генерує пару ключів RSA і створює цифровий підпис повідомлення.
Продемонструвати різницю між гешуванням і шифруванням.

"""

import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


def demo_hashing(text):
    print("\n--- 1. SHA-256 Гешування ---")
    data_bytes = text.encode('utf-8')
    sha_signature = hashlib.sha256(data_bytes).hexdigest()
    print(f"Вхідний текст: {text}")
    print(f"SHA-256 Геш: {sha_signature}")
    print("Спроба 'розшифрувати' геш неможлива (це одностороння функція).")


def demo_aes_encryption(text):
    print("\n--- 2. AES Симетричне шифрування ---")
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    encoded_text = text.encode('utf-8')
    encrypted_text = cipher_suite.encrypt(encoded_text)
    decrypted_text = cipher_suite.decrypt(encrypted_text)

    print(f"Оригінал: {text}")
    print(f"Ключ: {key}")
    print(f"Зашифровано: {encrypted_text}")
    print(f"Розшифровано: {decrypted_text.decode('utf-8')}")


def demo_rsa_signature(text):
    print("\n--- 3. RSA Цифровий підпис ---")
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()

    data = text.encode('utf-8')

    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print(f"Повідомлення: {text}")
    print(f"Цифровий підпис (hex): {signature.hex()[:50]}...")

    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Перевірка підпису: Успішно (Дані автентичні)")
    except Exception:
        print("Перевірка підпису: Помилка")


message = "Секретне повідомлення"

demo_hashing(message)
demo_aes_encryption(message)
demo_rsa_signature(message)
