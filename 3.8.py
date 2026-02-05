"""

Завдання 8. Створити програму «Графіка», яка містить полотно (Canvas) розміром
600×400 пікселів. Програма повинна дозволяти користувачу рисувати кола або лінії
за допомогою миші. Передбачити можливість вибору кольору рисування через
colorchooser, кнопку «Очистити» для очищення полотна та функцію збереження
зображення у файл формату .ps.

"""

import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Графіка - Python Tkinter")
        self.root.geometry("700x500")

        self.current_color = "black"
        self.tool = "line"
        self.start_x = None
        self.start_y = None
        self.current_shape_id = None

        control_frame = tk.Frame(root, bg="#ddd", pady=5)
        control_frame.pack(side="top", fill="x")

        btn_color = tk.Button(control_frame, text="Обрати колір", command=self.choose_color)
        btn_color.pack(side="left", padx=5)

        tk.Label(control_frame, text="Інструмент:", bg="#ddd").pack(side="left", padx=10)
        
        self.tool_var = tk.StringVar(value="line")
        rb_line = tk.Radiobutton(control_frame, text="Лінія (Олівець)", variable=self.tool_var, value="line", bg="#ddd")
        rb_line.pack(side="left")
        
        rb_circle = tk.Radiobutton(control_frame, text="Коло", variable=self.tool_var, value="circle", bg="#ddd")
        rb_circle.pack(side="left")

        btn_clear = tk.Button(control_frame, text="Очистити", command=self.clear_canvas, bg="#ffcccc")
        btn_clear.pack(side="right", padx=5)

        btn_save = tk.Button(control_frame, text="Зберегти (.ps)", command=self.save_image, bg="#ccffcc")
        btn_save.pack(side="right", padx=5)

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white", cursor="crosshair")
        self.canvas.pack(pady=10, expand=True)

        self.canvas.bind("<Button-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)

    def choose_color(self):
        color = colorchooser.askcolor(title="Оберіть колір")[1]
        if color:
            self.current_color = color

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".ps",
                                                 filetypes=[("PostScript", "*.ps")])
        if file_path:
            self.canvas.postscript(file=file_path, colormode='color')
            messagebox.showinfo("Збережено", f"Файл успішно збережено:\n{file_path}")

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.tool = self.tool_var.get()

        if self.tool == "circle":
            self.current_shape_id = self.canvas.create_oval(
                event.x, event.y, event.x, event.y, outline=self.current_color, width=2
            )

    def on_mouse_drag(self, event):
        if self.tool == "line":
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, 
                                    fill=self.current_color, width=2, capstyle=tk.ROUND, smooth=True)
            self.start_x = event.x
            self.start_y = event.y

        elif self.tool == "circle":
            if self.current_shape_id:
                self.canvas.coords(self.current_shape_id, self.start_x, self.start_y, event.x, event.y)

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
