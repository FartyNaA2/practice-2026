"""

Завдання 7. Створити структуру даних, що зберігає інформацію про групу студентів.
Для кожного студента передбачити поля: ім’я, прізвище, оцінки з п’яти навчальних
дисциплін. Реалізувати програму, яка виводить таблицю із середнім балом кожного
студента та обчислює середній бал групи з кожної дисципліни.

"""

students = [
    {
        "name": "Олександр", 
        "surname": "Коваленко", 
        "grades": [90, 85, 92, 88, 95]
    },
    {
        "name": "Марія", 
        "surname": "Бондаренко", 
        "grades": [95, 98, 100, 97, 99]
    },
    {
        "name": "Дмитро", 
        "surname": "Шевченко", 
        "grades": [75, 80, 72, 85, 78]
    },
    {
        "name": "Анна", 
        "surname": "Ткаченко", 
        "grades": [88, 90, 85, 92, 89]
    }
]

subjects = ["Математика", "Фізика", "Історія", "Програмування", "Англійська"]
num_subjects = 5
group_subject_sums = [0] * num_subjects

print(f"{'Прізвище':<15} {'Ім`я':<12} {'Оцінки':<25} {'Сер. бал':<10}")
print("-" * 65)

for student in students:
    grades = student["grades"]
    avg_score = sum(grades) / len(grades)
    
    grades_str = ", ".join(map(str, grades))
    
    print(f"{student['surname']:<15} {student['name']:<12} {grades_str:<25} {avg_score:<10.2f}")
    
    for i in range(num_subjects):
        group_subject_sums[i] += grades[i]

print("-" * 65)
print("Середній бал групи з кожної дисципліни:")

num_students = len(students)
for i in range(num_subjects):
    subject_avg = group_subject_sums[i] / num_students
    print(f"{subjects[i]}: {subject_avg:.2f}")
