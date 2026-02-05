"""

Завдання 2. Створити клас Student з атрибутами ім’я, група, середній_бал та методом
show_info(), який виводить повну інформацію про студента. Створити декілька
об’єктів цього класу і вивести інформацію про кожного.

"""

class Student:
    def __init__(self, name, group, avg_score):
        self.name = name
        self.group = group
        self.avg_score = avg_score

    def show_info(self):
        print(f"Студент: {self.name}, Група: {self.group}, Середній бал: {self.avg_score}")

student1 = Student("Олександр Бондаренко", "ІПЗ-21", 92.5)
student2 = Student("Марія Ткаченко", "КН-22", 89.4)
student3 = Student("Дмитро Шевченко", "КІ-23", 75.0)

student1.show_info()
student2.show_info()
student3.show_info()
