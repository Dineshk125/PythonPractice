## access Modifiers
## Public -
## Private - We define in using ( __ ) like -> __AccountNumber
## Protected - define in using single underscore ( _ ) like _Balance


from random import randint


class Bank:

    def __init__(self):
        self.__account_number = randint(1000, 9999)
        self.name = input("Enter Your Name: ")
        self.__Balance = 0

    def displayBalance(self):
        print(self.__Balance)

    def setBalance(self, newAmount):
        self.__Balance = newAmount

    def Display(self):
        print(f"your Account Number: {self.__account_number}")
        print(f"Your Name : {self.name}")
        print(f"Father Bank Balance : {self.__Balance} ")


c1 = Bank()

c1.Display()
c1.setBalance(100000000000)
c1.displayBalance()
