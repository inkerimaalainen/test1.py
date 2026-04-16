N = int(input('Введите число: '))
i = 1
a = 1
sum = 0
while a <= N:
    sum += i**2
    i += 1
    a += 1
print(sum)