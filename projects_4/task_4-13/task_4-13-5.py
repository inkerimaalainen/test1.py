l = []
a = input('Введите число: ')
while a != '':
    l.append(int(a))
    a = input('Введите число: ')

m = l[0]
i = 1
a = 1
for i in range(1, len(l)):
    if l[i] > m:
        m = l[i]
        a = i + 1
print('Максимальное число: ', m)