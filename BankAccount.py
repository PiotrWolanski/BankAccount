class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

account1 = BankAccount()
account2 = BankAccount()
account1.deposit(1000)
print(account1.balance)
print(account2.balance)
