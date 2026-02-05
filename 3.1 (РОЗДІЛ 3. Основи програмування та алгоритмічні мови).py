"""

Завдання 1. Створити програму, яка відкриває вікно з фіксованими розмірами
1024х768, заголовком «Перша програма», написом «Hello, world!» та має
завершувати свою роботу після натискання кнопки «Закрити».

"""

import tkinter as tk

root = tk.Tk()
root.title("Перша програма")
root.geometry("1024x768")
root.resizable(False, False)

label = tk.Label(root, text="Hello, world!", font=("Arial", 24))
label.pack(expand=True)

button = tk.Button(root, text="Закрити", command=root.destroy, font=("Arial", 14))
button.pack(pady=50)

root.mainloop()
