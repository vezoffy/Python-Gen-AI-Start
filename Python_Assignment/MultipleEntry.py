from Account import Account
from DebitAccount import DebitAccount
from CreditAccount import CreditAccount

accounts = []

accounts.append(Account(1, "John Doe", 1000.00))
accounts.append(DebitAccount(2, "Jane Doe", 2000.00, "password123"))
accounts.append(CreditAccount(3, "Bob Smith", 500.00, 0, 0))

print("Account 1 balance:", accounts[0].getBalance())
print("Account 2 balance:", accounts[1].getBalance())
print("Account 3 balance:", accounts[2].getBalance())