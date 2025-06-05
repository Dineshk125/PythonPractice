class Animal:

    def sound(self):
        print("Natural Sound")


class Dog(Animal):

    def sound(self):
        print("Bhaw Bhaw Bhaw Bhaw ")


class Cat(Animal):

    def sound(self):
        print("Meow meow meow meow")


c1 = Dog()

c1.sound()
