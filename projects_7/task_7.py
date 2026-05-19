import pandas as pd

import numpy as np

 

# Два класса с одинаковым средним, но разным разбросом

class_A = pd.Series([74, 75, 75, 76, 74, 75, 76, 75])   # «стабильный» класс

class_B = pd.Series([40, 55, 65, 80, 90, 95, 82, 93])   # «вариативный» класс

 

print('=== Класс A ===')

print(f'  Оценки:   {class_A.tolist()}')

print(f'  Среднее:  {class_A.mean():.1f}')
print(f'Медиана:    {class_A.mean():.2f}')
print(f'Дисперсия:  {class_A.var():.2f}')
print(f'    СКО:    {class_A.std():.2f}')
print(f'  Мин:      {class_A.min()}  |  Макс: {class_A.max()}')

 

print()

print('=== Класс B ===')

print(f'  Оценки:   {class_B.tolist()}')

print(f'Среднее:    {class_B.mean():.1f}')

print(f'Медиана:    {class_B.mean():.2f}')
print(f'Дисперсия:  {class_B.var():.2f}')
print(f'    СКО:    {class_B.std():.2f}')
print(f'  Мин:      {class_B.min()}  |  Макс: {class_B.max()}')


print()

print('Вывод: среднее одинаково — но классы очень разные!')