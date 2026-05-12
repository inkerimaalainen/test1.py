phenotype_d = input("Введите фенотип группы крови донора(I, II, III, IV): ").strip().upper()
if phenotype_d == "I":
    print("Группа крови: 0 (I)")
elif phenotype_d == "II":
    print("Группа крови: A (II)")
elif phenotype_d == "III":
    print("Группа крови: B (III)")
elif phenotype_d == "IV":
    print("Группа крови: AB (IV)")
else:
    print("Такой группы крови не существует")

phenotype_a = input("Введите фенотип группы крови пациента(I, II, III, IV): ").strip().upper()
if phenotype_a == "I":
    print("Группа крови: 0 (I)")
elif phenotype_a == "II":
    print("Группа крови: A (II)")
elif phenotype_a == "III":
    print("Группа крови: B (III)")
elif phenotype_a == "IV":
    print("Группа крови: AB (IV)")
else:
    print("Такой группы крови не существует")

if phenotype_d == phenotype_a or phenotype_d == 'I':
    print('Переливание крови возможно')
else:
    print('Переливание крови невозможно')
