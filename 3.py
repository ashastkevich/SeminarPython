"""
Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
"""
n = int(input("Введите номер четверти: "))
if n == 1:
    print("X > 0, Y > 0")
elif n == 2:
    print("X < 0, Y > 0")
elif n == 3:
    print("X < 0, Y < 0")
elif n == 4:
    print("X > 0, Y < 0")