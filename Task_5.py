# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти растояние в 3D пространстве)
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

from math import sqrt

def main():
    x1 = coord_x()
    y1 = coord_y()
    x2 = coord_x()
    y2 = coord_y()
    find_distance_2d(x1, y1, x2, y2)

def coord_x():
    return int(input("Введите координату Х: "))

def coord_y():
    return int(input("Введите координату Y: "))

def find_distance_2d(x1, y1, x2, y2):
    print (round(sqrt((x2 - x1)**2 + (y2 - y1)**2), 2))

main()