"""

Завдання 4. Створити клас Car з атрибутами марка, рік_випуску, пробіг і методами
drive(km) для збільшення пробігу та info() для виведення опису авто. Додати
конструктор init() і метод str() для зручного текстового відображення об’єкта.

"""

class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def drive(self, km):
        if km > 0:
            self.mileage += km
            print(f"Авто проїхало {km} км. Теперішній пробіг: {self.mileage} км.")
        else:
            print("Кількість кілометрів має бути додатною!")

    def info(self):
        print(f"Марка: {self.brand}, Рік випуску: {self.year}, Пробіг: {self.mileage} км")

    def __str__(self):
        return f"Автомобіль {self.brand} ({self.year}) — {self.mileage} км"

my_car = Car("Toyota Camry", 2020, 45000)
my_car.info()
my_car.drive(500)

print(f"Текстове представлення об'єкта: {my_car}")
