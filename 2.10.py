"""

Завдання 10. Додати до одного чи кількох створених класів властивості (@property)
для контролю коректності зміни атрибутів, зокрема заборонити встановлення
від’ємних значень там, де це нелогічно (наприклад, баланс або пробіг).

"""

class Car:
    def __init__(self, model, year, mileage):
        self.model = model
        self.year = year
        self._mileage = 0
        self.mileage = mileage

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value < 0:
            print(f"Помилка: Пробіг не може бути від'ємним! (Спроба встановити: {value})")
        elif value < self._mileage:
            print(f"Помилка: Новий пробіг ({value}) не може бути меншим за попередній ({self._mileage})!")
        else:
            self._mileage = value
            print(f"Пробіг успішно оновлено: {self._mileage} км")

    def info(self):
        print(f"Авто: {self.model} ({self.year}), Пробіг: {self._mileage} км")

print("--- Створення авто ---")
my_car = Car("Ford Mustang", 2022, 5000)

print("\n--- Коректна зміна пробігу ---")
my_car.mileage = 5500

print("\n--- Спроба встановити від'ємне значення ---")
my_car.mileage = -100

print("\n--- Спроба 'скрутити' пробіг (встановити менше значення) ---")
my_car.mileage = 2000

print("\n--- Фінальний стан ---")
my_car.info()
