# run from Python_Assignment folder
import orm_mapping
from orm_mapping import init_mappings, save, get_by_id, list_all, delete
from DebitAccount import DebitAccount
from CreditAccount import CreditAccount
from Account import Account

# create tables
init_mappings()

# create instances of your original classes
a1 = Account(1, "John Doe", 1000.0)
a2 = DebitAccount(2, "Jane Doe", 2000.0, "password123")
a3 = CreditAccount(3, "Bob Smith", 500.0, 0, 0)

# persist them via ORM (your class instances are mapped)
save(a1)
save(a2)
save(a3)

# query back
print(get_by_id(2).to_string(show_password=True))          # returns the DebitAccount instance
for a in list_all():
    print(a.accountNum, a.accountOwner, a.balance, getattr(a, 'bonusPoint', None))