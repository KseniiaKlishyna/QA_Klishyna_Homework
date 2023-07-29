# 1 Реалізуйте біблиотеку з будь-яким функціоналом.
# Наприклад, створіть функції для арифметичних операцій і побудуйте каскад імпортів з декількох packagів.
# Має бути можливіcть імпортувати деякі функції з пакета, але не всі.
import package_3
import datetime
print(package_3.square(4))

# 2 Створіть обробку одного будь-якого exception, який не використався як приклад на занятті.
# Виведіть результат в консоль
def divide (a,b):
    try:
        if a >= b:
            return a / b
    except Exception:
        print("b cannot be equal to 0 ")
    else:
        print("a must be greater than or equal to b")

print(divide(9,1))

# 3 Реалізуйте функцію, яка додає або віднімає від заданої дати певну кількість днів.
# Приймає на вхід будь-яку дату та час (datetime), а також значення днів(int), і знак(True або False, які репрезентують + і -).
# Повертає datetime. В цій задачі скористайтесь datetime.timedelta

date_1 = datetime.datetime(year=2023,month=7,day=30,hour=13,minute=56,second=33)
date_2 = datetime.timedelta(days=123, hours=17, minutes=9)
a = (input("Write + or -:"))
if a == "+":
    date_3 = date_1 + date_2
else:
    date_3 = date_1 - date_2
print(date_3)

# 4 Реалізуйте функцію, яка вираховує ваш точний вік(не обов'язково вказувати свої данні), вираховуючі різницю між наданим значеням і значенням datetime.now().
# Приймає дату та час(datetime), повертає два значення: datetime і datetime.timestamp.
# В цій задачі скористайтесь для конвертації datetime.timestamp. Виведіть результат в консоль

birthday = datetime.datetime(year=1997, month=12, day= 30)
now = datetime.datetime.now()
age = now.year - birthday.year
if birthday.month >= now.month and birthday.day > now.day:
    age -= 1
print(age)
print(datetime.datetime.timestamp(birthday))
print(datetime.datetime.timestamp(now))