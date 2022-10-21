num = input("логин")
num1 = input("пароль")
while(num != "12345678" or num1 != "123456789"):
    if (num != "12345678" and num1=="123456789")  :
        print(" login ne verniy")
    if (num == "12345678" and num1 !="123456789"):
        print("parol ne verni")
    if (num !="12345678" and num1 !="123456789"):
        print("login i  parol neverni")
    num = input("логин")
    num1 = input("пароль")
print("маладес")
    