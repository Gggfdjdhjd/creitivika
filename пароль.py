password = "123456789"
for i in range(10):
    user_pass = str(input("Введите пароль\n-> "))
    if password ==user_pass:
        print("Вы ввели правильный пароль")
        break
        #smt
    elif i == 9:
        print("попытки закончились")
    else:
        continue
        