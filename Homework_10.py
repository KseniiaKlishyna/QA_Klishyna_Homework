from abc import abstractmethod, ABC
class Vehicle(ABC):
    def __init__(self, name, wheels, body_type, brand):
        self.name = name
        self.wheels = wheels
        self.body_type = body_type
        self.brand = brand

    @abstractmethod
    def customization(self):
        pass

class Auto(Vehicle):
    def __init__(self, name, wheels: int, body_type, brand):
        super().__init__(name, wheels, body_type, brand)


class Crossover(Auto):
    def __init__(self, name, wheels: int, body_type, brand):
        super().__init__(name, wheels, body_type, brand)

    def customization(self):
        self.body_type = "Customized Crossover"
        print("You changed bodytype to: " + str(self.body_type))


class Sedan(Auto):
    def __init__(self, name, wheels: int, body_type , brand):
        super().__init__(name, wheels, body_type , brand)

    def customization(self):
        self.brand = "New sedan brand"
        print("You changed brand to: " + str(self.brand))


vehicle_1 = Crossover("Tutu", 4, "crossover", "Toyota")
vehicle_2 = Sedan("Rocket", 4, "sedan", "Mustang")

print(vehicle_1.customization())
print(vehicle_2.customization())
