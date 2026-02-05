"""

Завдання 8. Виконати завдання 7 із застосуванням бібліотеки Pandas, зберігаючи дані
про студентів у зовнішньому файлі.

"""

import pandas as pd

data = {
    "Прізвище": ["Коваленко", "Бондаренко", "Шевченко", "Ткаченко"],
    "Ім'я": ["Олександр", "Марія", "Дмитро", "Анна"],
    "Математика": [90, 95, 75, 88],
    "Фізика": [85, 98, 80, 90],
    "Історія": [92, 100, 72, 85],
    "Програмування": [88, 97, 85, 92],
    "Англійська": [95, 99, 78, 89]
}

df = pd.DataFrame(data)

file_name = "students_pandas.csv"
df.to_csv(file_name, index=False, encoding='utf-8')
print(f"Дані успішно збережено у файл '{file_name}'.\n")

try:
    df_loaded = pd.read_csv(file_name)

    subjects = ["Математика", "Фізика", "Історія", "Програмування", "Англійська"]

    df_loaded["Середній бал"] = df_loaded[subjects].mean(axis=1)

    print("Таблиця успішності:")
    print(df_loaded.to_string(index=False, float_format="%.2f"))

    print("\n------------------------------")
    print("Середній бал групи по предметах:")
    group_averages = df_loaded[subjects].mean()

    for subject, score in group_averages.items():
        print(f"{subject}: {score:.2f}")

except FileNotFoundError:
    print("Помилка: файл не знайдено.")
