from Homework_13.singleton import singleton

# 1 опишіть 1 будь-який клас, за умови що буде існувати тільки один інстанс цього класу.
@singleton
class Candy_Sun:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

candy_1 = Candy_Sun("Sonechko", "AVK", 23)
candy_2 = Candy_Sun("Romashka", "Roshen", 22)
print(candy_1.name)
print(candy_2.brand)

# 2 опишіть частину функціоналу замовлення в ресторані. OrderPart класс має метод, що повертає певне блюдо.


from Homework_13.drivers.dishes import Dish
from Homework_13.drivers.drinks import Drink

class OrderPart:
    @staticmethod
    def get_menu (menu):
        if menu == 'dish':
            return Dish()
        elif menu == 'drink':
            return Drink()

customer_1 = OrderPart.get_menu('dish')
order_1 = customer_1.order('Pizza')
print(order_1)