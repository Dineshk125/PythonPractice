## Public -
## Private - We define in using ( __ ) like -> __AccountNumber
## Protected - define in using single underscore ( _ ) like _Balance

from random import randint


class Father:

    def __init__(self):
        self.account_number = randint
        self.name = input("Father Name : ")
        self._acc_balance = int(input("Enter Father Account Balance: "))
        self.__mobile = input("Enter Phone Model: ")

    def __str__(self):
        return f"Father Account Number : {self.account_number} \n Father Name:{self.name} \n Father Account Balance : {self._acc_balance} \n Father Phone Model: {self.__mobile}"


c1 = Father()
c2 = Father()
print()
print(c1)
print()
print(c2)
print()
