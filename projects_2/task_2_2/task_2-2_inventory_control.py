reagent_name = input('Enter the reagent name: ')
reagent_count = int(input('Enter the amount of reagent(only number please): '))
#c is correct
reagent_name_c = reagent_name.lower()
f = open('inventory.txt', 'w', encoding = 'utf-8')
print(f'Реактив {reagent_name_c} поступил на склад в количестве {reagent_count} шт.', file = f)
f.close()
print(f'Реактив {reagent_name_c} поступил на склад в количестве {reagent_count} шт.')
