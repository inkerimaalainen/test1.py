#all - все элементы таблицы(+заголовок), elements, full_element_1 - левые элементы таблицы, full_element_2 - все правые элементы таблицы
#ввод левых элементов таблицы и заголовка

title = input('Enter the sheet title: ')
elements = []
print("Enter the element's names(press enter to finish): ")
while True:
    element = input()
    elements.append(element)
    if element == '':
        del elements[-1]
        break

#список с заголовком и всеми элементами таблицы
all = []
all.append(title)
m = 0
while m != len(elements):
    all.append(elements[m])
    m += 1

#ввод правых элементов таблицы
a = 0
while a < len(elements):
    element = input(f'Enter the {''.join(elements[a])}(press enter to finish): ')
    a += 1
    all.append(element)
    if element =='':
        del all[-1]
        break


s1 = int((len(all)+1)/2)
s2 = int(len(all))

#вывод элементов таблицы
full_element_1 = []
full_element_2 = []
g = 0
while s1 < len(all) or g < len(elements):
    full_element_1.append(elements[g])
    full_element_2.append(all[s1])
    g += 1
    s1 += 1


f = []
t = 0
while t < len(full_element_1):
    f.append(len(f'| {full_element_1[t]} \t {full_element_2[t]} |') * ' ')
    t += 1

#border = '+' + ((len(max(full_element_1) + max(full_element_2)) + len('\t') + 4) * '-') + '+'
border = '+' + len(max(f)) * '-' + '+'
print(f'{border}\n| {title + (len(border) - len(title) - 4) * ' '} |\n{border}')
t = 0
while t < len(full_element_1):
    print(f'| {full_element_1[t]} {((len(border) - len(f[t])) + 1) * ' '} {full_element_2[t]} |')
    t += 1

print(border)
