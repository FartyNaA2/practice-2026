"""

Завдання 6. Створити програму «Блокнот», яка дозволяє відкривати, редагувати та
зберігати текстові файли. Реалізувати меню з пунктами «Відкрити», «Зберегти» та
«Вийти». Для вибору файлу використати діалогові вікна askopenfilename і
asksaveasfilename. При закритті програми без збереження має з’являтися
попередження.

"""

import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    text_area.delete(1.0, tk.END)
    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()
        text_area.insert(tk.END, text)
    root.title(f"Блокнот - {filepath}")

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w", encoding="utf-8") as output_file:
        text = text_area.get(1.0, tk.END)
        output_file.write(text)
    root.title(f"Блокнот - {filepath}")

def on_closing():
    if messagebox.askyesno("Вихід", "Ви впевнені, що хочете вийти? Незбережені дані можуть бути втрачені."):
        root.destroy()

root = tk.Tk()
root.title("Блокнот")
root.geometry("800x600")

text_area = tk.Text(root, font=("Arial", 12))
text_area.pack(expand=True, fill="both")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)

file_menu.add_command(label="Відкрити", command=open_file)
file_menu.add_command(label="Зберегти", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Вийти", command=on_closing)

menu_bar.add_cascade(label="Файл", menu=file_menu)

root.config(menu=menu_bar)
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
