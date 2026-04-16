a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
d = int(input('Введите число d: '))
m = a
if m > b:
    m = b
else:
    if m > c:
        m = c
    else:
        if m > d:
            m = d
print(m)