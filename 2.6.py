"""

Завдання 6. Створити базовий клас Animal із методом sound() і похідні класи Dog,
Cat, Cow, що перевизначають цей метод для відтворення власного звуку.

"""

class Animal:
    def sound(self):
        print("Тварина видає звук")

class Dog(Animal):
    def sound(self):
        print("Гав-гав!")

class Cat(Animal):
    def sound(self):
        print("Мяу!")

class Cow(Animal):
    def sound(self):
        print("Му-у-у!")

dog = Dog()
cat = Cat()
cow = Cow()

print("Собака:")
dog.sound()

print("Кіт:")
cat.sound()

print("Корова:")
cow.sound()
