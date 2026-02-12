#В ходе эксперимента выявлены нарушения умственных способностей студента, студент был поражён вирусом вайбкодинга

name = input('Введите ФИО исследователя: ')
date = input('Введите дату исследования: ')
exp = input('Введите название эксперимента: ')
conc = input('Напишите вывод исследования: ')
a = list(conc)


border = '+' + 50 * '-' + '+'
title = 'Электронный лабораторный журнал'
title_c = title + (49 - len(title)) * ' ' + '|'
name_c = name + (49 - len(name) - len('ФИО исследователя : ')) * ' ' + '|'
date_c = date + (49 - len(date) - len('Дата исследования : ')) * ' ' + '|'
exp_c = exp + (49 - len(exp) - len('Эксперимент : ')) * ' ' + '|'


with open('journal.txt', 'w', encoding = 'utf-8') as card:


    card.write(f'{border}\n| {title_c}\n{border}\n| ФИО исследователя : {name_c}\n| Дата исследования : {date_c}\n| Эксперимент : {exp_c}')
    n = 0
    m = 48
    while m <= len(a):
        card.write(f'\n| {''.join(a[n:m])} |')
        n += 47
        m += 47
    card.write(f'\n| {''.join(a[len(a) - (len(a) % 48) - 1:len(a)])}' + (48 - (len(a) % 48)) * ' ' + '|')
    card.write(f'\n{border}')