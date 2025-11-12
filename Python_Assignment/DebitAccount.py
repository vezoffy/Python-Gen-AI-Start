from Account import Account

class DebitAccount(Account):
    def __init__(self, accountNum, accountOwner, balance, password):
        super().__init__(accountNum, accountOwner, balance)
        self.password = password

    def performDeposit(self, amount, password):
        if password == self.password:
            self.balance += amount
        else:
            print("Invalid password.")

    def performPayment(self, amount, password):
        if password == self.password:
            self.balance -= amount
        else:
            print("Invalid password.")

    def getPassword(self):
        return self.password
    
    def getBalance(self):
        return self.balance

    def __repr__(self):
        return (f"DebitAccount(accountNum={self.accountNum!r}, accountOwner={self.accountOwner!r}, "
                f"balance={self.balance!r}, password={'***' if self.password else None})")

    def __str__(self):
        return f"DebitAccount #{self.accountNum} ({self.accountOwner}) - balance: {self.balance} - password: {'***' if self.password else None}"

    def to_string(self, show_password: bool = True) -> str:
        """Return a printable representation. By default the password is masked.

        Pass show_password=True to include the actual password value.
        """
        pwd = self.password if show_password else ('***' if self.password else None)
        return f"DebitAccount #{self.accountNum} ({self.accountOwner}) - balance: {self.balance} - password: {pwd}"
        