"""

Завдання 5. Створити програму з кількома вкладками (Notebook), які мають назви
«Головна», «Налаштування» та «Про програму». У вкладці «Головна» розмістити
форму введення даних, у «Налаштування» — вибір кольору фону за допомогою
colorchooser, а у вкладці «Про програму» — інформацію про автора. Реалізувати
збереження вибраного кольору при повторному запуску.

"""

import tkinter as tk
from tkinter import ttk, colorchooser, messagebox
import json
import os

CONFIG_FILE = "settings.json"

def load_settings():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                return data.get("bg_color", "#f0f0f0")
        except Exception:
            return "#f0f0f0"
    return "#f0f0f0"

def save_settings(color):
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump({"bg_color": color}, f)
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося зберегти налаштування: {e}")

def update_background(color):
    tab_main.config(bg=color)
    tab_settings.config(bg=color)
    tab_about.config(bg=color)
    
    global current_color
    current_color = color

def choose_color():
    color_code = colorchooser.askcolor(title="Оберіть колір фону")[1]
    
    if color_code:
        update_background(color_code)
        save_settings(color_code)
        lbl_current_color.config(text=f"Поточний колір: {color_code}")

root = tk.Tk()
root.title("Програма з вкладками")
root.geometry("400x300")

current_color = load_settings()

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

tab_main = tk.Frame(notebook, bg=current_color)
notebook.add(tab_main, text="Головна")

tk.Label(tab_main, text="Форма введення даних", font=("Arial", 12, "bold"), bg=current_color).pack(pady=10)
tk.Label(tab_main, text="Ваше ім'я:", bg=current_color).pack()
entry_name = tk.Entry(tab_main)
entry_name.pack(pady=5)

tk.Label(tab_main, text="Електронна пошта:", bg=current_color).pack()
entry_email = tk.Entry(tab_main)
entry_email.pack(pady=5)

tk.Button(tab_main, text="Відправити", command=lambda: messagebox.showinfo("Інфо", "Дані відправлено!")).pack(pady=10)

tab_settings = tk.Frame(notebook, bg=current_color)
notebook.add(tab_settings, text="Налаштування")

tk.Label(tab_settings, text="Налаштування інтерфейсу", font=("Arial", 12, "bold"), bg=current_color).pack(pady=20)

lbl_current_color = tk.Label(tab_settings, text=f"Поточний колір: {current_color}", bg=current_color)
lbl_current_color.pack(pady=5)

btn_color = tk.Button(tab_settings, text="Змінити колір фону", command=choose_color)
btn_color.pack(pady=10)

tab_about = tk.Frame(notebook, bg=current_color)
notebook.add(tab_about, text="Про програму")

tk.Label(tab_about, text="Інформація про автора", font=("Arial", 12, "bold"), bg=current_color).pack(pady=20)
tk.Label(tab_about, text="Розробник: Студент групи ІПЗ-XX", bg=current_color).pack(pady=5)
tk.Label(tab_about, text="Рік розробки: 2023", bg=current_color).pack(pady=5)
tk.Label(tab_about, text="Версія: 1.0", bg=current_color).pack(pady=5)

update_background(current_color)

root.mainloop()
