name = input('Введите название питательной среды: ')
conc = input('Введите концентрацию агара(%): ')
temp = input('Введите температуру стерилизации(ºС): ')
with open('recipe.txt', 'w', encoding = 'utf-8') as card:
    card.write(f'{name}\nКонцентрация:\t{conc}\nТемпература стерилизации:\t{temp}')
print('Файл "recipe.txt" успешно сформирован!')
