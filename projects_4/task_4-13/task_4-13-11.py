l = []
sum = 0
a = 0
while True:
    n = input('Введите число: ')
    if (not n):
        break
    l.append(int(n))

for i in range(len(l)):
    if i % 2 == 0:
        sum += l[i]
        a += 1

print(sum/a)