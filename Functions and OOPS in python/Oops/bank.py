# Simple bank user details find

from random import randint


class Bank:

    def __init__(self):
        self.account_no = randint(100000, 999999)
        self.name = input("Enter your Name: ")
        self.Phone_no = int(input("Enter Ypur phone number: "))
        self.balance = 0

    def showbalance(self):
        print(f"Current Balance = {self.balance}")

    def withdraw(self):
        amount = float(input("Enter amount To withdraw: "))
        if amount > self.balance:
            print("Insuficient balance.")
        else:
            self.balance -= amount

    def deposit(self):
        amount = float(input("Enter amount to Deposit: "))
        self.balance += amount


b1 = Bank()

b1.showbalance()
b1.deposit()
b1.showbalance()
b1.withdraw()
b1.showbalance()

# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Simple bank user details find using list and objects

# -----------------------------------------------------------------------------------------------------------------------------------------------------

from random import randint


class Bank:

    def __init__(self):
        self.account_no = randint(100000, 999999)
        self.name = input("Enter your Name: ")
        self.Phone_no = int(input("Enter Ypur phone number: "))
        self.balance = 0

    def showbalance(self):
        print(f"Current Balance = {self.balance}")

    def withdraw(self):
        amount = float(input("Enter amount To withdraw: "))
        if amount > self.balance:
            print("Insuficient balance.")
        else:
            self.balance -= amount

    def deposit(self):
        amount = float(input("Enter amount to Deposit: "))
        self.balance += amount


Banks = []
x = Bank()
Banks.append(x)
print(Banks)


y = Bank()
Banks.append(y)
print(Banks)

Banks[0].showbalance()
Banks[1].deposit()
Banks[1].withdraw()
Banks[1].showbalance()

# ----------------------------------------------------------------------------------------------------------------------------------------------------


# fatch bank details using while loop


# -----------------------------------------------------------------------------------------------------------------------------------------------------

from random import randint


class Bank:

    def __init__(self):
        self.account_no = randint(100000, 999999)
        self.name = input("Enter Your Name: ")
        self.Phone_no = int(input("Enter Your Phone Number: "))
        self.balance = 0

    def show_info(self):
        print(f"Account Number : {self.account_no}")
        print(f"Name : {self.name}")
        print(f"Phone Number : {self.Phone_no}")
        print(f"Account Balance  : {self.balance} \n")

    def showbalance(self):
        print(f"Current Balance = {self.balance}")

    def withdraw(self):
        amount = float(input("Enter Amount To Withdraw: "))
        if amount > self.balance:
            print("Insuficient Balance.")
        else:
            self.balance -= amount

    def deposit(self):
        amount = float(input("Enter Amount To Deposit: "))
        if amount >= 0:
            self.balance += amount
        else:
            print("Invalid Deposit Amount")


Banks = []

while True:
    print("1. Create Account.")
    print("2. Show Bank Details.")
    print("3. Deposit Amount.")
    print("4. Withdraw Amount")
    print("5. Exit. \n")

    choice = int(input("Enter Your Choice.: "))
    if choice == 1:
        obj = Bank()
        Banks.append(obj)
        print(Banks)
    elif choice == 2:
        if len(Banks) == 0:
            print("NO Account Found")
        else:
            for accounts in Banks:
                accounts.show_info()
    elif choice == 3:
        if len(Banks) == 0:
            print("No Any Account Found Yet.")
        else:
            acc_no = int(input("Enter Account Number To Deposit: \n"))
            for obj in Banks:
                factor = 0
                if acc_no == obj.account_no:
                    obj.deposit()
                    factor += 1
            if factor == 0:
                print("Account Number Does Not Exist.")

    elif choice == 4:
        if len(Banks) == 0:
            print("No Bank Fount To Withdraw.")
        else:
            acc_no = int(input("Enter Account Number To Withdraw : \n"))
            for obj in Banks:
                if obj.account_no == acc_no:
                    obj.withdraw()
                    break

    elif choice == 5:
        break
    else:
        print("Invalid Choice. \n")


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# add method to transfer amounnt from one account to another account


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from random import randint


class Bank:

    def __init__(self):
        self.account_no = randint(100000, 999999)
        self.name = input("Enter Your Name: ")
        self.Phone_no = int(input("Enter Your Phone Number: "))
        self.balance = 0

    def show_info(self):
        print(f"Account Number : {self.account_no}")
        print(f"Name : {self.name}")
        print(f"Phone Number : {self.Phone_no}")
        print(f"Account Balance  : {self.balance} \n")

    def showbalance(self):
        print(f"Current Balance = {self.balance}")

    def withdraw(self):
        amount = float(input("Enter Amount To Withdraw: "))
        if amount > self.balance:
            print("Insuficient Balance.")
        else:
            self.balance -= amount

    def deposit(self):
        amount = float(input("Enter Amount To Deposit: "))
        if amount >= 0:
            self.balance += amount
        else:
            print("Invalid Deposit Amount")


Banks = []


def check_acc_exist(acc_no):
    global Banks

    for obj in Banks:
        if obj.account_no == acc_no:
            return obj
    return None


while True:
    print("1. Create Account.")
    print("2. Show Bank Details.")
    print("3. Deposit Amount.")
    print("4. Withdraw Amount.")
    print("5. Transfar Amount.")
    print("6. Exit. \n")

    choice = int(input("Enter Your Choice.: "))
    if choice == 1:
        obj = Bank()
        Banks.append(obj)
        print(Banks)
    elif choice == 2:
        if len(Banks) == 0:
            print("NO Account Found")
        else:
            for accounts in Banks:
                accounts.show_info()
    elif choice == 3:
        if len(Banks) == 0:
            print("No Any Account Found Yet.")
        else:
            acc_no = int(input("Enter Account Number To Deposit: "))
            for obj in Banks:
                factor = 0
                if acc_no == obj.account_no:
                    obj.deposit()
                    factor += 1
            if factor == 0:
                print("Account Number Does Not Exist.")

    elif choice == 4:
        if len(Banks) == 0:
            print("No Bank Fount To Withdraw.")
        else:
            acc_no = int(input("Enter Account Number To Withdraw : "))
            for obj in Banks:
                if obj.account_no == acc_no:
                    obj.withdraw()
                    break
    elif choice == 5:
        from_acc_no = int(
            input("Enter Account Number From Which You Want To Transfer Amount: ")
        )

        to_acc_no = int(
            input("Enter Which Account Number To Which You Want To Transfer Amount: ")
        )

        from_acc_obj = check_acc_exist(from_acc_no)
        to_acc_obj = check_acc_exist(to_acc_no)

        if from_acc_obj != None and to_acc_obj != None:
            transfer_amount = int(input("Enter Transfer Amount: "))
            if from_acc_obj.balance < transfer_amount:
                print("Insuficient Balance.")
            else:
                from_acc_obj.balance -= transfer_amount
                to_acc_obj.balance += transfer_amount
        else:
            print("Account Does Not Exist")

    elif choice == 6:
        break
    else:
        print("Invalid Choice. \n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Other method -> one Acc to Other acc transfer amount

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

from random import randint


class Bank:

    def __init__(self):
        self.account_no = randint(100000, 999999)
        self.name = input("Enter Your Name: ")
        self.Phone_no = int(input("Enter Your Phone Number: "))
        self.balance = 0

    def show_info(self):
        print(f"Account Number : {self.account_no}")
        print(f"Name : {self.name}")
        print(f"Phone Number : {self.Phone_no}")
        print(f"Account Balance  : {self.balance} \n")

    def showbalance(self):
        print(f"Current Balance = {self.balance}")

    def withdraw(self):
        amount = float(input("Enter Amount To Withdraw: "))
        if amount > self.balance:
            print("Insuficient Balance.")
        else:
            self.balance -= amount

    def deposit(self):
        amount = float(input("Enter Amount To Deposit: "))
        if amount >= 0:
            self.balance += amount
        else:
            print("Invalid Deposit Amount")


Banks = []

while True:
    print("1. Create Account.")
    print("2. Show Bank Details.")
    print("3. Deposit Amount.")
    print("4. Withdraw Amount.")
    print("5. Transfar Amount.")
    print("6. Exit. \n")

    choice = int(input("Enter Your Choice.: "))
    if choice == 1:
        obj = Bank()
        Banks.append(obj)
        print(Banks)
    elif choice == 2:
        if len(Banks) == 0:
            print("NO Account Found")
        else:
            for accounts in Banks:
                accounts.show_info()
    elif choice == 3:
        if len(Banks) == 0:
            print("No Any Account Found Yet.")
        else:
            acc_no = int(input("Enter Account Number To Deposit: "))
            for obj in Banks:
                factor = 0
                if acc_no == obj.account_no:
                    obj.deposit()
                    factor += 1
            if factor == 0:
                print("Account Number Does Not Exist.")

    elif choice == 4:
        if len(Banks) == 0:
            print("No Bank Fount To Withdraw.")
        else:
            acc_no = int(input("Enter Account Number To Withdraw : "))
            for obj in Banks:
                if obj.account_no == acc_no:
                    obj.withdraw()
                    break
    if choice == 5:
        if len(Banks) == 0:
            print("There is no account found.\nFirst, create a account.")
        else:
            Sender_acc_num = int(
                input("For Transction, Enter Sender's(Your) Account no. : ")
            )
            Sender_found = 0
            for Sender_obj in Banks:
                if Sender_acc_num == Sender_obj.account_no:
                    Receiver_acc_num = int(
                        input("For Transction, Enter Receiver's Account no. : ")
                    )
                    Receiver_found = 0
                    for Receiver_obj in Banks:
                        if Receiver_acc_num == Receiver_obj.account_no:
                            Receiver_found += 1
                            transfer_amount = int(
                                input("For Transfer, Enter the amount : ")
                            )
                            if transfer_amount <= Sender_obj.balance:
                                Sender_obj.balance -= transfer_amount
                                Receiver_obj.balance += transfer_amount
                                print(
                                    f"{transfer_amount}Rs. transferd Successfully from {Sender_obj.name}  to {Receiver_obj.name}."
                                )
                            else:
                                print("Insuficient bank balance.")

                    if Receiver_found == 0:
                        print("Receiver's Account does not exist.")
                    Sender_found += 1

            if Sender_found == 0:
                print("Sender's Account does not exist.")
    elif choice == 6:
        break
