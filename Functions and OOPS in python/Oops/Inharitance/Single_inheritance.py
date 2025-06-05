class Car:

    def __init__(self):
        self.color = input("Enter Car Color: ")
        self.type = input("Enter Car Type: ")
        self.milage = float(input("Enter Milege Per KM : "))
        self.seat_capacity = int(input("Enter Seat Capacity of Car : "))

    def car_info(self):
        print(f"Color = {self.color}")
        print(f"type = {self.type}")
        print(f"milage = {self.milage}")
        print(f"seat capacity = {self.seat_capacity}")


class Audi(Car):
    def __init__(self):
        super().__init__()
        self.electic = input("Enter Car Electric or Not: ")
        self.city = input("Enter Which City You Buy Car: ")
        print()

    def audi_info(self):
        print(f"Electric = {self.electic}")
        print(f"City = {self.city}")

    def show_full_info(self):
        self.car_info()
        self.audi_info()


c1 = Audi()

c1.show_full_info()
