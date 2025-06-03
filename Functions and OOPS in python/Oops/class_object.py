# class :--> it is an blue print of object
# object :---> it is an instence of classs which means accessibility by the object of classs


class student:
    # Attributes / class Variable / class attributes

    id = 0
    name = ""
    age = 0
    gender = ""

    def info(self):
        print(f"id = {self.id}")
        print(f"name = {self.name}")
        print(f"age ={self.age}")
        print(f"gender = {self.gender}")


s1 = student()
s1.name = "Dinesh"
s1.age = 23
s1.gender = "Male"
s1.id = 101

s1.info()


# using Method


class student:

    id = 0
    name = ""
    age = 0
    gender = ""

    def get_info(self):
        print(f"id = {self.id}")
        print(f"name = {self.name}")
        print(f"age ={self.age}")
        print(f"gender = {self.gender}")

    def set_info(self):
        # using Methods -> in class defining a
        self.id = int(input("Enter your ID : "))
        self.name = input("Enter your name : ")
        self.age = int(input("Enter your age : "))
        self.gender = input("Enter your Gender : ")


s1 = student()
s2 = student()

s1.set_info()
s1.get_info()

s2.set_info()
s2.get_info()


# using init method


class student:

    def __init__(self):  # Initializer
        self.id = int(input("Enter your ID : "))
        self.name = input("Enter your name : ")
        self.age = int(input("Enter your age : "))
        self.gender = input("Enter your Gender : ")

    def info(self):
        print(f"id = {self.id}")
        print(f"name = {self.name}")
        print(f"age ={self.age}")
        print(f"gender = {self.gender}")


s1 = student()
s2 = student()


s1.info()
s2.info()
