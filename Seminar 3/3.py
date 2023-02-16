"""
Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу 
между максимальным и минимальным значением 
дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
my_list = [2.31, 1.24, 3.11, 1.2, 3.04, 4.12]
max_num = min_num = my_list[0]-int(my_list[0])
for i in my_list:
    if (i-int(i)) > max_num: max_num = (i-int(i))
    if (i-int(i)) < min_num: min_num = (i-int(i))
    print(max_num, min_num)
print(round(max_num - min_num,10))