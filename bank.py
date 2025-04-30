# create a bank acc simulation write a python program to class bank acc with method 1.Deposit 2.Withdraw 3. check_balnce

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"{self.owner}'s current balance: ₹{self.balance}")

# Example usage
account = BankAccount("Alice")

account.deposit(5000)
account.withdraw(1200)
account.check_balance()
