while True:
    n = int(input("Введіть число від 1 до 10: "))
    if 1 <= n <= 10:
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
        break
    else:
        print("Неправильне число, спробуйте ще раз.")