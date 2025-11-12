from Account import Account;
from CreditAccount import CreditAccount;
from DebitAccount import DebitAccount;

acc1: Account = CreditAccount(1, "John Doe", 1000.00, 0, 0)
acc2: Account = DebitAccount(2, "Jane Doe", 2000.00, "password123")

acc1.performDeposit(100.00)
acc2.performPayment(50.00, "password123")

print("Account 1 balance:", acc1.getBalance())
print("Account 2 balance:", acc2.getBalance())
print("Account 2 password:", acc2.getPassword())
print("Account 1 bonus points:", acc1.getBonusPoint())
print("Account 1 limit:", acc1.getLimit())