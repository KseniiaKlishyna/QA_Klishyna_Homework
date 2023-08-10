from abc import ABC, abstractmethod
import random

class Museum(ABC):
    def __init__(self,name, author, age: int, renovation ):
        self.__name = name
        self.author = author
        self.age = age
        self.renovation = renovation

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @abstractmethod
    def renovate(self):
        pass

    @staticmethod
    def number_of_staff_required():
        number = random.randint(1, 9)
        return number

class Art(Museum):
    def __init__(self,name, author, age: int, renovation ):
        super().__init__(name, author, age, renovation )

    def __prepare_for_renovation(self):
        print( "All preparations are ready")

    def __prepare_staff(self):
        print("Art staff is prepared")

    def __finish(self):
        print("Almost done!")
    def renovate(self):
        self.__prepare_for_renovation()
        self.__prepare_staff()
        self.__finish()
        self.renovation = "renovated"
        print("Art is " + str(self.renovation))



class Sculpture(Museum):
    def __init__(self,name, author, age: int, renovation ):
        super().__init__(name, author, age, renovation )

    def __prepare_for_renovation(self):
        print("All preparations are ready")

    def __prepare_staff(self):
        print("Sculpture staff is prepared")

    def __sculpture_update(self):
        print("Special sculpture works are done!")

    def __finish(self):
        print("Almost done!")

    def renovate(self):
        self.__prepare_for_renovation()
        self.__prepare_staff()
        self.__sculpture_update()
        self.__finish()
        self.renovation = "renovated"
        print("Sculpture is " + str(self.renovation))

item_1 = Art("Mona Lisa","Da Vinci" , 519, "")
item_2 = Sculpture("David", "Michelangelo", 520, "")

item_1.name = "New Mona Lisa"
item_1.renovate()
item_2.renovate()
print(item_1.name)
print(item_2.number_of_staff_required())
