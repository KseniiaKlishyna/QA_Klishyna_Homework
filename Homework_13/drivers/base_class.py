from abc import ABC, abstractmethod
class Menu(ABC):
    _name = ''
    @abstractmethod
    def order(self, name):
        pass