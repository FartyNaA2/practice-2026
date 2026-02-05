"""

Завдання 2. Розробити програму, яка перетворює числове значення у рядкове
представлення без використання вбудованої функції str().

"""

DIGITS = "0123456789"

try:
    number = int(input("Введіть ціле число: "))
    output = ""
    is_negative = False   
    if number == 0:
        output = "0"
    else:
        if number < 0:
            is_negative = True
            number = -number 
        while number > 0:
            digit = number % 10  
            output = DIGITS[digit] + output  
            number = number // 10       
        if is_negative:
            output = "-" + output
    print("Результат:", output)
    print("Тип результату:", type(output))    
except ValueError:
    print("Помилка: введіть коректне ціле число.")
