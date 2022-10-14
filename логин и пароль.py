flag = False
for xgdfgfdhdf in range(3):
    login = input("- Логин: ")
    password = input("- Пароль : ")
    if (login == 'admin' and password == 'trGd3j'):
        flag = True
        break
if flag:
    print('Авторизация пройдена с попытки', xgdfgfdhdf + 1)
else:
    print('Доступ запрещён')