password = "password123"
while True:
    inp = input("Введіть пароль: ")
    if inp == password:
        print("Ви увійшли в систему.")
        break
    else:
        print("Неправильний пароль.")