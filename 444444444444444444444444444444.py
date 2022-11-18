#lower() приводит к нижнему регистру — можно писать
# не только «выход», но и «Выход» и хоть «ВыХоД» —
# всё приведётся в «выход»
comand = input("Введите командуууууу").lower()

while comand != "выход":
    if comand == "анек":
        print("заходит короче улитка в бар")
        print("ну и бармен её вышвыривает")
        print("через неделю улитка приходит и спрашивает")
        print("ну и зачем ты это сделал")
        if comand =="песня":
            print("зачем мне солцееееееее")
            print("манакоооооооооооооооооооооо")
            print("тгкимзкумкуук")
            print("я дальше не помню")
    elif comand == "барабере":
        slovo = input("Введите любое слово")
        print("барабере"+slovo)
    elif comand == "боба":
        slovo = input("введите что та акзоазйц")
        print("тебе нельзя"+slovo)
    elif comand == "беба":
        slovo = input("введитеощшкумщукшмццку")
        print("съешь"+slovo)
    elif comand == "биба":
        slovo = input("введите что та акзоазйц")
        print("узбек?"+slovo)
    elif comand=="калькулятор":
        a=input("vvedi deistvie")
        if a == "+":
            b=int(input("pervoe chislo"))
            n=int(input("vtoroe chislo"))
            print(b+n)
        elif a == "-":
            b=int(input("pervoe chislo"))
            n=int(input("vtoroe chislo"))
            print(b-n)
        elif a == "*":
            b=int(input("pervoe chislo"))
            n=int(input("vtoroe chislo"))
            print(b*n)
        elif a == "/":
            b=int(input("pervoe chislo"))
            n=int(input("vtoroe chislo"))
            print(b/n)
    comand = input("Введите команду").lower()
print("Чат-бот спит")