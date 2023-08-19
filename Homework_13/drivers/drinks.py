from Homework_13.drivers.base_class import Menu

class Drink(Menu):
    _name = 'drink'

    def __init__(self):
        self.__positions = ['Water', 'Juice', 'Wine']

    @property
    def positions(self):
        return self.__positions

    def order(self,name):
        if name == 'Water':
            return 'Here is your water'
        elif name == 'Juice':
            return 'Here is your juice'
        elif name == 'Wine':
            return 'Here is your wine'
        else:
            return 'We do not have this position in menu'