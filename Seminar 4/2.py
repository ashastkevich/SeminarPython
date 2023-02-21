"""
Задайте натуральное число N.
Напишите программу, которая составит
список простых множителей числа N.
"""
number = n = int(input("Введите натуральное число: "))
factors = set()
i = 2
while i * i <= n:
    if n % i:
        i += 1
    else:
        n //= i
        factors.add(i)
if n > 1:
    factors.add(n)
print("Список простых множителей числа", number, ":", factors)