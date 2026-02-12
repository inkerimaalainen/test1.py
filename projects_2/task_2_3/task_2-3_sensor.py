name = input('Введите имя оператора: ')
pressure  = input('Введите текующее значение давления(Па): ')
with open('sensor_log.txt', 'w', encoding = 'utf-8') as card:
    card.write(f'{name} \t {pressure} Па')
print('Данные успешно сохранены в sensor_log.txt')