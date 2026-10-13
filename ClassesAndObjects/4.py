"""
Create a BankAccount class that stores an account holder's name and balance.
Add instance methods to deposit money, withdraw money, and display the balance.
Do not allow a withdrawal greater than the available balance.
"""


class BankAccount:
    def __init__(self, name, bal):
        self.name = name
        self.bal = bal

    def deposit(self, amt): 
        self.bal += amt
        print(f"Deposited {amt}. New balance: {self.bal}")
       

    def withdraw(self, amt):
        if amt > self.bal:
            print("Insufficient balance.")
        else:
            self.bal -= amt
            print(f"Withdrew {amt}. Remaining balance: {self.bal}")

    def display_balance(self):
        print(f"Account holder: {self.name}")
        print(f"Current balance: {self.bal}")


acc = BankAccount("Kaku", 6767)
acc.display_balance()
acc.deposit(1900)
acc.withdraw(8181)
acc.withdraw(2000)
acc.display_balance()

