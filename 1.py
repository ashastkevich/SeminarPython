"""
Задание 1
Напишите программу, которая принимает на вход цифру,
обозначающую день недели, и проверяет, 
является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет
"""
n = int(input("Введите день недели: "))
if n == 6 or n == 7:
    print('Да')
else:
    print("Нет")