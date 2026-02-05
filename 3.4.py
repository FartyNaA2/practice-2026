"""

Завдання 4. Створити програму «Калькулятор», яка дозволяє вводити два числа та
виконувати основні арифметичні операції: додавання, віднімання, множення та
ділення. Результат обчислень має відображатися у полі Label. Забезпечити обробку
помилок — зокрема, випадок ділення на нуль або введення нечислових значень.

"""

import tkinter as tk

def calculate(operation):
    try:
        val1 = float(entry_num1.get())
        val2 = float(entry_num2.get())
        result = 0

        if operation == "+":
            result = val1 + val2
        elif operation == "-":
            result = val1 - val2
        elif operation == "*":
            result = val1 * val2
        elif operation == "/":
            if val2 == 0:
                label_result.config(text="Помилка: ділення на 0", fg="red")
                return
            result = val1 / val2

        label_result.config(text=f"Результат: {result}", fg="black")

    except ValueError:
        label_result.config(text="Помилка: введіть коректні числа", fg="red")

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x250")

tk.Label(root, text="Перше число:").pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

tk.Label(root, text="Друге число:").pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="+", width=5, command=lambda: calculate("+")).pack(side="left", padx=5)
tk.Button(frame_buttons, text="-", width=5, command=lambda: calculate("-")).pack(side="left", padx=5)
tk.Button(frame_buttons, text="*", width=5, command=lambda: calculate("*")).pack(side="left", padx=5)
tk.Button(frame_buttons, text="/", width=5, command=lambda: calculate("/")).pack(side="left", padx=5)

label_result = tk.Label(root, text="Результат: ", font=("Arial", 12, "bold"))
label_result.pack(pady=20)

root.mainloop()
