"""
Вычислить число pi c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

"""
import math
PI_CONST = 3.1415926535
n = int(input("Введите необходимую точность (от 1 до 10): "))
PI_n = round(PI_CONST,n)
pi = 0
i = 0
while PI_n != round(pi,n):
    pi += 4 * (-1)**i / (2*i + 1)
    i += 1
print(f"Pi равно {round(pi,n)}")