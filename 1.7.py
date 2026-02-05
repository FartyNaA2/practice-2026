"""

Завдання 7. Створити структуру даних, що зберігає інформацію про групу студентів.
Для кожного студента передбачити поля: ім’я, прізвище, оцінки з п’яти навчальних
дисциплін. Реалізувати програму, яка виводить таблицю із середнім балом кожного
студента та обчислює середній бал групи з кожної дисципліни. напиши щерез це завдання 

"""

class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def get_average(self):
        return sum(self.grades) / len(self.grades)

students = [
    Student("Іван", "Петренко", [90, 85, 92, 88, 95]),
    Student("Марія", "Коваль", [100, 98, 95, 99, 100]),
    Student("Олег", "Сидоренко", [75, 80, 78, 82, 70]),
    Student("Анна", "Бойко", [88, 90, 85, 92, 89]),
    Student("Дмитро", "Гнатюк", [60, 65, 70, 68, 72])
]

print(f"{'Прізвище та Ім\'я':<20} | {'Оцінки (1-5 предмети)':<25} | {'Сер. бал':<10}")
print("-" * 65)

subject_sums = [0] * 5

for student in students:
    avg = student.get_average()
    grades_str = ", ".join(map(str, student.grades))
    
    print(f"{student.last_name} {student.first_name:<20} | {grades_str:<25} | {avg:.2f}")

    for i in range(5):
        subject_sums[i] += student.grades[i]

print("-" * 65)

group_averages = [s / len(students) for s in subject_sums]
group_avg_str = ", ".join([f"{x:.1f}" for x in group_averages])

print(f"{'СЕРЕДНЄ ПО ПРЕДМЕТАХ':<20} | {group_avg_str:<25} |")
