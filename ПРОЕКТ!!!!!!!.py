#lower() приводит к нижнему регистру — можно писать
# не только «выход», но и «Выход» и хоть «ВыХоД» —
# всё приведётся в «выход»
import random
g = ["заходит как то раз улитка в бар \n и бармен её вышвыривает \n через неделю она приходит и спрашивает \n ну и зачем ты это сделал", "колобок повесился", "приходит черепаха в бар \n просит стакан воды \n и так несколько дней подряд \n через неделю таких походов бармен спрсил \n может тебе сока налить \n а черепаха ему в ответ \n погоди мужик у меня дом горит", "буратино утонул"]
h = ["в моих глазах горит квазар \n иду вперёд ни шагу назад \n кидаю степ лечу на старт \n весь твой профит идет на спад", "укращаю эти волны словно гио томиока \n достаю клинок из ножен \n их окутала тревога \n я несусь по головам и оставляю следы крови \n режу все врагов катаной этот мир такой суровый", "ялялляляляляляляля", "тишка сан ларан весит на мне за сотку \n но я всё еще обычная девченка \n брюлики картье я вставила в заколку \n соса мьюзик бэйби еду по району"]
m = ["z","x","c","v","b","n","m","l","k","j","h","g","f","d","s","a","p","o","i","u","y","t","r","e","w","q","1","2","3","4","5","6","7","8","9","0"]
comand = input("Введите командуууууу").lower()

while comand != "выход":
    if comand == "анек":
        print(g[random.randint(0,3)])

    if comand =="песня":
        print(h[random.randint(0,3)])
           
           
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
        elif a == "//":
            b=int(input("pervoe chislo"))
            n=int(input("vtoroe chislo"))
            print(b//n)
        elif a == "%":
            b=int(input("pervoe chislo"))
            n=int(input("vtoroe chislo"))
            print(b%n)
        elif a == "**":
            b=int(input("pervoe chislo"))
            n=int(input("vtoroe chislo"))
            print(b**n)
            
            
    comand = input("Введите команду").lower()
print("Чат-бот спит")