from Account import Account

acc1 = Account(1, "John Doe", 1000.00)
acc2 = Account(2, "Jane Doe", 2000.00) 

acc1.performDeposit(100.00)
acc2.performPayment(50.00)

print("Account 1 balance:", acc1.getBalance())
print("Account 2 balance:", acc2.getBalance())