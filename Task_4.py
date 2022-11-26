#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def main():
    possible_coord(get_quarter())

def get_quarter():
    while True:
        quarter = int(input("Введите номер четверти: "))
        if 0 < quarter <= 4:
            return quarter

def possible_coord(number):
    if number == 1:
        print ("х(0, ∞), y(0, ∞)")
    elif number == 2:
        print ("х(-∞, 0), y(0, ∞)")
    elif number == 3:
        print("х(-∞, 0), y(-∞, 0)")
    elif number == 4:
        print("х(0, ∞), y(-∞, 0)")

main()