# # Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

def main():
    is_weekend(ask_number())

def ask_number():
    return int(input("Введите число: "))

def is_weekend(number):
    match number:
        case 1 | 2 | 3 | 4 | 5:
            print("нет")
        case 6 | 7:
            print("да")
        case _:
            print("введено некорректное число")

main()