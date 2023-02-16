"""
Задайте число. Составьте список чисел Фибоначчи,
в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""
k = int(input("Введите число: "))
if k == 0:
    fib_list = [0]
    print(fib_list)
elif k == 1:
    fib_list = [1, 0, 1]
    print(fib_list)
elif k == 2:
    fib_list = [-1, 1, 0, 1, 1]
    print(fib_list)
else:
    fib_list = [-1, 1, 0, 1, 1]
    for i in range(2, k):
        fib_list.append(fib_list[-2]+fib_list[-1])
        fib_list.insert(0,int(((-1)**(-i))*fib_list[len(fib_list)-1]))
    print(fib_list)