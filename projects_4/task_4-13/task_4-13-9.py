l = []
sum = 0
while True:
    n = input('Введите число: ')
    if (not n):
        break
    l.append(int(n))




for i in range(len(l)):
    if l[i] % 2 != 0:
        sum += l[i]

print(sum)