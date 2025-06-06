from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def sound(self):
        print("abc")
        pass


class Audi(Car):
    def __init__(self, engin):
        self.ingin = engin

    def sound(self):
        print("Sport sound")


# c = Audi("1200cc")
# c.sound()

# c = Car()
