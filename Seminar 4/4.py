"""
Задана натуральная степень k. 
Сформировать случайным образом
список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
import random
k = int(input("Введите натуральную степень k: "))
polynomial_list = []
for i in range(k,0,-1):
    multiplier = random.randint(0,10)
    if multiplier:
        polynomial_list.append(str(multiplier)+"*x^"+str(i))
print(' + '.join(polynomial_list), "= 0")