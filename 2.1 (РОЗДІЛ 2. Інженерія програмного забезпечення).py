"""

Завдання 1. Написати коротку програму для обчислення площі кількох фігур
(наприклад, прямокутник, коло) у двох підходах: процедурному (окремі функції) та
об’єктно-орієнтованому (класи з методами area()).

"""

import math

def area_rectangle(width, height):
    return width * height

def area_circle(radius):
    return math.pi * radius ** 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

print("--- Процедурний підхід ---")
w, h = 10, 5
r = 7
print(f"Площа прямокутника (10x5): {area_rectangle(w, h)}")
print(f"Площа кола (r=7): {area_circle(r):.2f}")

print("\n--- Об'єктно-орієнтований підхід ---")
rect_obj = Rectangle(10, 5)
circle_obj = Circle(7)
print(f"Площа прямокутника (10x5): {rect_obj.area()}")
print(f"Площа кола (r=7): {circle_obj.area():.2f}")
