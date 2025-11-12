class Account:
    def __init__(self, accountNum, accountOwner, balance):
        self.accountNum = accountNum
        self.accountOwner = accountOwner
        self.balance = balance
    
    def performDeposit(self, amount):
        self.balance += amount
    
    def performPayment(self, amount):
        self.balance -= amount
    
    def getBalance(self):
        return self.balance

    def __repr__(self):
        return f"Account(accountNum={self.accountNum!r}, accountOwner={self.accountOwner!r}, balance={self.balance!r})"

    def __str__(self):
        return f"Account #{self.accountNum} ({self.accountOwner}) - balance: {self.balance}"