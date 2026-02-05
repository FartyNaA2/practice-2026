import tkinter as tk

class MainWindow:
    def __init__(self, root, logic_callback):
        self.root = root
        self.logic_callback = logic_callback
        
        self.root.title("Модульна програма")
        self.root.geometry("400x250")

        tk.Label(root, text="Введіть текст:").pack(pady=10)
        
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        btn = tk.Button(root, text="Обробити", command=self.on_button_click)
        btn.pack(pady=10)

        self.result_label = tk.Label(root, text="Результат: ", fg="blue", font=("Arial", 12))
        self.result_label.pack(pady=20)

    def on_button_click(self):
        user_input = self.entry.get()
        processed_text, count = self.logic_callback(user_input)
        self.result_label.config(text=f"Текст: {processed_text}\nСимволів: {count}")
