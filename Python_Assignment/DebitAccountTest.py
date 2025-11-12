from DebitAccount import DebitAccount

acc1 = DebitAccount(1, "John Doe", 1000.00, "password123")

acc1.performDeposit(100.00, "password123")
acc1.performPayment(50.00, "password123")

print("Account 1 balance:", acc1.getBalance())
print("Account 1 password:", acc1.getPassword())