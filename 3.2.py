"""

Завдання 2. Створити програму, яка містить три кнопки: «Привітати», «Очистити» та
«Вийти». При натисканні на кнопку «Привітати» у вікні має з’являтися текст «Вітаю,
користувач!». Кнопка «Очистити» повинна видаляти цей текст, а «Вийти» —
закривати програму. Реакцію на натискання реалізувати через механізм подій
(command).

"""

import tkinter as tk

def show_greeting():
    label_message.config(text="Вітаю, користувач!")

def clear_message():
    label_message.config(text="")

root = tk.Tk()
root.title("Кнопки та події")
root.geometry("300x250")

label_message = tk.Label(root, text="", font=("Arial", 14))
label_message.pack(pady=30)

btn_greet = tk.Button(root, text="Привітати", command=show_greeting, width=20)
btn_greet.pack(pady=5)

btn_clear = tk.Button(root, text="Очистити", command=clear_message, width=20)
btn_clear.pack(pady=5)

btn_exit = tk.Button(root, text="Вийти", command=root.destroy, width=20)
btn_exit.pack(pady=5)

root.mainloop()
