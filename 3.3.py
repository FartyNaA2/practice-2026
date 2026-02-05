"""

Завдання 3. Створити програму «Анкета користувача», яка містить поля для введення
імені, вибору статі (чоловіча або жіноча), прапорець «Погоджуюсь із умовами» та
кнопку «Зберегти». Після натискання кнопки в окремому полі повинна відображатися
інформація, введена користувачем. Розміщення елементів здійснити за допомогою
менеджера grid.

"""

import tkinter as tk

def save_data():
    name = entry_name.get()
    gender = var_gender.get()
    agreed = var_agree.get()

    if agreed:
        result_text = f"Ім'я: {name}\nСтать: {gender}\nСтатус: Умови прийнято"
        label_output.config(text=result_text, fg="green")
    else:
        label_output.config(text="Ви повинні погодитись із умовами!", fg="red")

root = tk.Tk()
root.title("Анкета користувача")
root.geometry("300x300")

tk.Label(root, text="Введіть ім'я:").grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Оберіть стать:").grid(row=1, column=0, padx=10, pady=5, sticky="w")

var_gender = tk.StringVar(value="Чоловіча")
tk.Radiobutton(root, text="Чоловіча", variable=var_gender, value="Чоловіча").grid(row=1, column=1, sticky="w")
tk.Radiobutton(root, text="Жіноча", variable=var_gender, value="Жіноча").grid(row=2, column=1, sticky="w")

var_agree = tk.BooleanVar()
tk.Checkbutton(root, text="Погоджуюсь із умовами", variable=var_agree).grid(row=3, column=0, columnspan=2, pady=10)

tk.Button(root, text="Зберегти", command=save_data).grid(row=4, column=0, columnspan=2, pady=5)

label_output = tk.Label(root, text="", font=("Arial", 10, "bold"))
label_output.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
