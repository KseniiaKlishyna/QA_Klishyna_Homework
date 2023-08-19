from Homework_13.drivers.base_class import Menu

class Dish(Menu):
    _name = 'dish'

    def __init__(self):
        self.__positions = ['Risotto', 'Pasta', 'Pizza']

    @property
    def positions(self):
        return self.__positions

    def order(self,name):
        if name == 'Risotto':
            return 'Here is your risotto'
        elif name == 'Pasta':
            return 'Here is your pasta'
        elif name == 'Pizza':
            return 'Here is your pizza'
        else:
            return 'We do not have this position in menu'


