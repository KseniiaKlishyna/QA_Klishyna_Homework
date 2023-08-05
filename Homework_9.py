import random

#1 Cтворіть класс з описом будь-якої тварини. Додайте 1 static method, 3 звичайних методи
class Dog:
    def __init__(self, name, age, color, status):
        self.name = name
        self.age = age
        self.color = color
        self.status = status
    @staticmethod
    def greeting():
        print("Hello friend!")
    def my_information(self):
        print("My name is " + self.name+ ". I'm " + self.color + " dog.")
    def check_status(self):
        if self.age <= 1:
            self.status = "Puppy"
        elif self.age > 1 and self.age < 5:
            self.status = "Adult"
        else:
            self.status = "Senior"
        return self.status
    def age_in_human_years(self):
        human_years = self.age * 12
        return human_years



emily = Dog("Emily", 12, "brown", "Empty")
brayan = Dog("Brayan", 4, "white", "Empty")
jack = Dog("Jack", 1, "gray", "Empty")

Dog.greeting()
emily.check_status()
brayan.check_status()
jack.check_status()

print(emily.status)
print(brayan.age_in_human_years())
print(jack.my_information())

#2 Створіть класс з описом будь-якої компанії чи організації.
# Додайте 1 classmethod, 3 звичайних методи

class Company:
    company_name = "FUN-SUN Company"
    def __init__(self, name, age, position, years_in_company, promotion):
        self.name = name
        self.age = age
        self.position = position
        self.years_in_company = years_in_company
        self.promotion = promotion

    @classmethod
    def company_info(cls):
        return cls.company_name
    def calculate_promotion(self):
        if self.years_in_company > 3:
             self.promotion = "waiting for promotion"
        else:
            self.promotion = "no promotion"
        return self.promotion
    def info(self):
        print("Name: " + (self.name)+
              " Age: " + str(self.age) +
              " Position: " + (self.position) +
              " Years in company: " + str(self.years_in_company) +
              " Additional info: " + (self.promotion))
    def change_position(self):
        new_position = str(input("Enter new title:  "))
        self.position = new_position
        return self.position

human_1 = Company("Anna", 34, "QA", 4, "-")
human_2 = Company("Bil", 29, "Designer", 2, "-")
human_3 = Company("Dan", 30, "Developer", 5, "-")

print(human_3.company_info())
human_1.calculate_promotion()
print(human_1.info())
human_2.change_position()
print(human_2.info())

#3 Створіть декоратор, який виводить в консоль ім'я функції, яку було ввикликано. Наприклад, створіть пару функцій для аріфметичних операцій додавання і множення.
# При виклику цих функцій має повертатись результат операції і виводиться в консоль ім'я функції, яку було ввикликано.

def add_title(function):
    def title(*args, **kwargs):
        print(f"{function.__name__}")
        result = function(*args, **kwargs)
        return result
    return title
@add_title
def multiply(a, b):
    result = a * b
    return result
@add_title
def addition(a, b):
    result = a + b
    return result

print(multiply(2,4))
print(addition(8,6))


#4 Створіть за допомогою list comprehension список, в якому буде 100 елементів, і кожен із яких буде в границях від 1 до 10(для цього можна скористатись функцією randint із модуля random).
# Порахуйте кількість кожного елемента і виведіть в консоль

list_comprehension = [random.randint(1, 10) for i in range(100)]
def count_elements(element):
    result = list_comprehension.count(element)
    print(str(element) + " is in list " + str(result) + " times.")

count_elements(10)