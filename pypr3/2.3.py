inp = int(input("Введіть ціле число щоб порахувати його факторіал: "))
if inp < 0:
    print("Факторіал від'ємного числа не визначений")
elif inp == 0:
    print("1")
else:
    fact = 1
    for i in range(1, inp + 1):
        fact *= i
    print(fact)