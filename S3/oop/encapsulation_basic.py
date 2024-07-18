class BankAccount:
    def __init__(self, balance):
        self.balance = balance




account = BankAccount(1000)
a = 1000
account.balance -= 1000
if a > 5000:
    account.balance -= 10


account.balance += 100
