n = input("Введите вещественное число: ")
sum = 0
for i in range(len(n)):
    if n[i] != "." and n[i] != ",":
        sum += int(n[i])
print(sum)