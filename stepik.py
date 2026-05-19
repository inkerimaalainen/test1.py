import sys

# Считываем число N
input_data = sys.stdin.read().split()


n = int(input_data[0])

# Находим позицию внутри повторяющегося цикла длины 8
remainder = n % 8

# Если остаток 0, это эквивалентно 8-му шагу цикла
if remainder == 0:
    remainder = 8
    
# Определяем номер пальца по его позиции в цикле
if remainder <= 5:
    # Идем вперед: 1->1, 2->2, 3->3, 4->4, 5->5
    print(remainder)
else:
    # Идем назад: 6->4 (безымянный), 7->3 (средний), 8->2 (указательный)
    print(10 - remainder)

