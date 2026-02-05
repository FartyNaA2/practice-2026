"""

Завдання 3. Реалізувати програму, що приймає на вхід оцінки студентів і
використовує вбудовані типи Python (list, dict, set) для обчислення середнього балу,
підрахунку унікальних оцінок і формування словника у форматі {ім’я: середній_бал}.

"""

students_data = {
    "Олексій": [85, 90, 82, 88, 95],
    "Марина": [95, 98, 100, 92, 96],
    "Дмитро": [60, 75, 68, 70, 72],
    "Наталія": [88, 90, 85, 92, 89]
}

final_report = {}
all_grades = []

print("Список оцінок студентів:")
for name, grades in students_data.items():
    print(f"{name}: {grades}")
    
    all_grades.extend(grades)
    
    average_score = sum(grades) / len(grades)
    final_report[name] = round(average_score, 2)

unique_grades = set(all_grades)

print("\n--- Аналіз успішності ---")
print(f"Сформований словник (Ім'я: Середній бал): {final_report}")
print(f"Всі унікальні оцінки в групі (Set): {unique_grades}")
print(f"Кількість унікальних оцінок: {len(unique_grades)}")
