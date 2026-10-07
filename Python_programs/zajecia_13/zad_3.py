class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f"Właściciel: {self.owner}, Saldo: {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            return f"Niewystarczająca ilość środków :("
        else:
            return f"Można przeprowadzić operację"

    def getbalance(self, owner):
        print(self.balance)

x = BankAccount("129576321", 10850)
print(x)
x.deposit(200)
print(x)
x.getbalance("129576321")




