## Public -
## Private - We define in using ( __ ) like -> __AccountNumber
## Protected - define in using single underscore ( _ ) like _Balance

from random import randint


class Father:

    def __init__(self):
        self.account_number = randint
        self.name = input("Father Name : ")
        self.__mobile = input("Enter Phone Model: ")
        self._acc_balance = int(input("Enter Father Account Balance: "))

    def desplayFather(self):
        print(f"Father Name:{self.name}")
        print(f"Father Account Number : {self.account_number}")
        print(f"Father Account Balance : {self._acc_balance}")
        print(f"Father Phone Model: {self.__mobile}")


class Child(Father):

    def __init__(self):
        super().__init__()
        self.child_name = input("Child Name : ")

    def displayChildInfo(self):
        print(f"Child Name:{self.child_name}")
        print(f"Father Account Number: {self.account_number}")
        print(f"father Balance: {self._acc_balance}")
        print(f"Father Name : {self.name}")
        # print(f"Father Phone:{self.__mobile}") ## AttributeError: 'Child' object has no attribute '_Child__mobile'


c1 = Child()

c1.displayChildInfo()
