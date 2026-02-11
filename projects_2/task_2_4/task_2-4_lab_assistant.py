#lab_ass is laboratory ASSISTANT

v_all = int(input('Введите нужный объём раствора(в мл): '))
m_s = v_all * 0.009
v_w = (v_all * 0.991) / 0.997
title = ' ОТЧЁТ ПО ПРИГОТОВЛЕНИЮ: '
border = (len(title) + 1) * '-'
print(f'{title}\n{border}\nОбщий объём:\t{v_all} мл\nМасса соли:\t{m_s:.2f} г\nОбъём воды:\t{v_w:.2f} мл')
with open('lab_ass.txt', 'w', encoding = 'utf-8') as lab_ass:
    lab_ass.write(f'{title}\n{border}\nОбщий объём:\t{v_all} мл\nМасса соли:\t{m_s:.2f} г\nОбъём воды:\t{v_w:.2f} мл')