from CreditAccount import CreditAccount

acc1 = CreditAccount(1, "John Doe", 1000.00, 0, 0)

acc1.performDeposit(100.00)
acc1.performPayment(50.00)

print("Account 1 balance:", acc1.getBalance())
print("Account 1 bonus points:", acc1.getBonusPoint())
print("Account 1 limit:", acc1.getLimit())