""""

Завдання 5. Написати програму, що здійснює сортування масиву методом
«бульбашкового сортування». Дані для масиву користувач вводить самостійно;
початкова довжина масиву не фіксована.

"""

try:
    user_input = input("Введіть числа масиву через пробіл: ")
    array = [int(x) for x in user_input.split()]
    n = len(array)

    print(f"Початковий масив: {array}")

    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    print(f"Відсортований масив: {array}")

except ValueError:
    print("Помилка: будь ласка, вводьте лише цілі числа, розділені пробілом.")
