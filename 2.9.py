"""

Завдання 9. Змоделювати предметну область на вибір (наприклад, «Бібліотека—
Книга—Читач» або «Зоопарк—Тварина—Доглядальник») так, щоб у рішенні були
присутні ієрархія класів, абстракція, інкапсуляція, наслідування та поліморфізм;
продемонструвати типові взаємодії об’єктів.

"""

from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self._is_available = True

    @abstractmethod
    def get_info(self):
        pass

    def check_availability(self):
        return self._is_available

    def set_availability(self, status):
        self._is_available = status

class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def get_info(self):
        status = "Доступна" if self._is_available else "Видана"
        return f"[Книга] '{self.title}' від {self.author}. Статус: {status}"

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def get_info(self):
        status = "Доступний" if self._is_available else "Виданий"
        return f"[Журнал] '{self.title}' №{self.issue_number}. Статус: {status}"

class Reader:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)
        print(f"До фонду додано: {item.title}")

    def show_catalog(self):
        print("\n--- Каталог бібліотеки ---")
        for item in self.__items:
            print(item.get_info())
        print("--------------------------")

    def lend_item(self, title, reader):
        for item in self.__items:
            if item.title == title:
                if item.check_availability():
                    item.set_availability(False)
                    print(f"Читач {reader.name} успішно взяв '{item.title}'.")
                    return
                else:
                    print(f"Вибачте, '{item.title}' зараз у іншого читача.")
                    return
        print(f"Елемент '{title}' не знайдено у бібліотеці.")

lib = Library()
b1 = Book("Кобзар", 101, "Т. Шевченко")
b2 = Book("1984", 102, "Дж. Орвелл")
m1 = Magazine("National Geographic", 201, 5)

lib.add_item(b1)
lib.add_item(b2)
lib.add_item(m1)

reader1 = Reader("Олексій")
reader2 = Reader("Марія")

lib.show_catalog()

lib.lend_item("Кобзар", reader1)
lib.lend_item("Кобзар", reader2)
lib.lend_item("1984", reader2)

lib.show_catalog()
