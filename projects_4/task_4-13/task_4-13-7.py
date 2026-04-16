l = []
i = 1
a = 1
sum = 0
n = input('Введите число: ')
while n != '':
    l.append(int(n))
    n = input('Введите число: ')

for i in range(len(l)):
    sum += l[i]
print(sum/len(l))