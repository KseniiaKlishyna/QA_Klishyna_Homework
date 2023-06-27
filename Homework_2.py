#Задача 1
"""
В змінній minute лежит число от 0 до 59, згенероване випадковим чином.
Визначте в якій четверті години попадає це число (в першій, другій, третій чи четвертій).
"""

"""
import random

minute = random.randint(0,59)
if minute <= 15:
    print("It's " + str(minute) + "\nThis is the first quarter of an hour")
elif minute <= 30 and minute > 15:
    print("It's " + str(minute) + "\nThis is the second quarter of an hour")
elif minute <=45 and minute > 30:
    print("It's " + str(minute) + "\nThis is the third quarter of an hour")
else:
    print("It's " + str(minute) + "\nThis is the fourth quarter of an hour")
"""

#Задача 2
"""
В змінній birth_month запишіть номер місяця вашого народження (дані введіть з консолі). 
В залежності від введених даних виведіть характеристику для відповідної пори року:
Зима - За вікном падав сніг.
Весна - Все довкола розцвітало.
Літо - Діти насолоджувались літніми канікулами.
Осінь - Все довкола загоралось яскравими фарбами.
"""

"""
birth_month = int(input("Введіть місяць Вашего народження: "))

if birth_month >= 1 and birth_month <= 12:
    if birth_month >= 3 and birth_month <6:
        print("Все довкола розцвітало.")
    elif birth_month >= 6 and birth_month <9:
        print("Діти насолоджувались літніми канікулами.")
    elif birth_month >= 9 and birth_month < 12:
        print("Все довкола загоралось яскравими фарбами.")
    else:
        print("За вікном падав сніг.")
else:
    print("Такого місяця не існує:)")
"""

#Задача 3
"""
 За введеними координатами з'ясувати, до якої координатної чверті належить точка. 
 ( Координати ввести з консолі, варто зауважити, що це можуть бути не лише цілі числа. 
 Опрацювати варіант, коли точка- початок координат або лежить на осі ) 
"""
a = float(input("Enter X: "))
b = float(input("Enter Y: "))

if a > 0:
    if b == 0:
        print("Точка лежить на осі X")
    elif b > 0:
        print("Точка належить до першої координатної чверті")
    else:
        print("Точка належить до четвертої координатної чверті")
elif a < 0:
    if b == 0:
        print("Точка лежить на осі X")
    elif b > 0:
        print("Точка належить до другої координатної чверті")
    else:
        print("Точка належить до третьої координатної чверті")
else:
    if b == 0:
        print("Точка лежить на початку координат")
    else:
        print("Точка лежить на осі Y")

