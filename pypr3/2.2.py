inp = input("Введіть числа через пробіл: ")
num_list = [int(x) for x in inp.split( )]
summation = sum(num_list)
print("Список чисел:", num_list)
print("Сума чисел:", summation)