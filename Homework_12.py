class Train:
    def __init__(self, name):
        self.name = name
        self.cars = {}

    def __len__(self):
        return len(self.cars)

    def __setitem__(self, number, car):
        self.cars[number] = car

    def __getitem__(self, item):
        return self.cars[item]

    def __str__(self):
        return f' Welcome on board {self.name}! This train contains {self.__len__()} cars!'

class TrainCar(Train):

    def __init__(self, number):
        self.number = number
        self.passengers = {}

    def __len__(self):
        return len(self.passengers)

    def __setitem__(self, number, name):
        self.passengers[number] = name

    def __getitem__(self, item):
        return self.passengers[item]

    def __str__(self):
        return f' There are {self.__len__()} passengers in the car number {self.number}'

class Passenger(TrainCar):

    def __init__(self, name, seat, destination):
        self.name = name
        self.seat = seat
        self.destination = destination


    def __str__(self):
        return f'Name: {self.name}\nSeat: {self.seat}\nDestination: {self.destination}'

train = Train("Kapitoshka")
car_1 = TrainCar(1)
car_2 = TrainCar(2)
car_3 = TrainCar(3)
train[1] = car_1
train[2] = car_2
train[3] = car_3
print(train)
passenger_1 = Passenger("Andy", "33B", "Kielce")
passenger_2 = Passenger("Mark", "09A", "Krakow")
passenger_3 = Passenger("Daisy", "44B", "Wroclaw")
passenger_4 = Passenger("Gigi", "16B", "Kielce")
passenger_5 = Passenger("Bob", "55A", "Poznan")
passenger_6 = Passenger("Stewe", "01A", "Lodz")
passenger_7 = Passenger("Ann", "86B", "Krakow")
passenger_8 = Passenger("Fabian", "77B", "Kielce")
passenger_9 = Passenger("Brian", "21B", "Poznan")
passenger_10 = Passenger("Rose", "02B", "Wroclaw")
passenger_11 = Passenger("Sam", "38A", "Wroclaw")
car_1[1] = passenger_1
car_1[2] = passenger_2
car_2[1] = passenger_3
car_2[2] = passenger_4
car_2[3] = passenger_5
car_2[4] = passenger_6
car_2[5] = passenger_7
car_2[6] = passenger_8
car_2[7] = passenger_9
car_3[1] = passenger_10
car_3[2] = passenger_11
print(car_1)
print(car_2)
print(car_3)
print(passenger_1)



