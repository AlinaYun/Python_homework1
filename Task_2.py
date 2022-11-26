# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def input_x():
    return int(input("Введите Х: "))

def input_y():
    return int(input("Введите Y: "))

def input_z():
    return int(input("Введите Z: "))

def check_statement(x, y, z):
    left = not (x or y or z)
    right = not x and not y and not z
    if left == right:
        print("выражение истинно")
    else:
        print("выражение ложно")

check_statement(input_x(), input_y(), input_z())