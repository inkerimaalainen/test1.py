l = []
sum = 0
while True:
    n = input('Введите число: ')
    if (not n):
        break
    l.append(int(n))


for i in l:
    if l[i] > 0:
        sum += 1
print(sum)