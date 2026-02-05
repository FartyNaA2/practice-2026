"""

Завдання 5. Реалізувати клас BankAccount із приватним атрибутом __balance,
методами deposit(amount) і withdraw(amount) та публічним методом get_balance() для
перегляду стану рахунку. Продемонструвати, як інкапсуляція захищає дані від прямої
зміни ззовні.

"""

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Рахунок поповнено на {amount}. Баланс: {self.__balance}")
        else:
            print("Сума поповнення повинна бути додатною.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Знято {amount}. Баланс: {self.__balance}")
        else:
            print("Недостатньо коштів або сума некоректна.")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)

print(f"Отримання балансу через публічний метод: {account.get_balance()}")

print("Спроба прямого доступу до приватного атрибута __balance:")
try:
    print(account.__balance)
except AttributeError:
    print("Помилка доступу: Атрибут '__balance' є приватним і недоступний ззовні.")
