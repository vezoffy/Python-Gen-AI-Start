from Account import Account
class CreditAccount(Account):
    def __init__(self, accountNum, accountOwner, balance, bonusPoint, limit):
        super().__init__(accountNum, accountOwner, balance)
        self.bonusPoint = bonusPoint
        self.limit = limit
    
    def performDeposit(self, amount):
        self.balance += amount
        self.bonusPoint += 1
        self.limit += 1
        self.balance += self.bonusPoint
    
    def performPayment(self, amount):
        self.balance -= amount
        self.bonusPoint += 1
        self.limit += 1
        self.balance += self.bonusPoint

    def getBalance(self):
        return self.balance
    
    def getBonusPoint(self):
        return self.bonusPoint
    
    def getLimit(self):
        return self.limit
    
    def __repr__(self):
        return (f"CreditAccount(accountNum={self.accountNum!r}, accountOwner={self.accountOwner!r}, "
                f"balance={self.balance!r}, bonusPoint={self.bonusPoint!r}, limit={self.limit!r})")

    def __str__(self):
        return (f"CreditAccount #{self.accountNum} ({self.accountOwner}) - balance: {self.balance}, "
                f"bonusPoint: {self.bonusPoint}, limit: {self.limit}")
    
