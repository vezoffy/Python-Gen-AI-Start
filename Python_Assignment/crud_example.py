from db import init_db
import repository


def main():
    # create DB and tables
    init_db()

    print("Creating sample accounts...")
    repository.create_account(1, "John Doe", 1000.0, account_type='base')
    repository.create_account(2, "Jane Doe", 2000.0, account_type='debit', password='password123')
    repository.create_account(3, "Bob Smith", 500.0, account_type='credit', bonus_point=0, limit=0)

    print("Listing accounts after creation:")
    for a in repository.list_accounts():
        print(f"id={a.id}, owner={a.owner}, balance={a.balance}, type={a.type}")

    print("Updating account 1 balance to 1500.0")
    repository.update_balance(1, 1500.0)
    a = repository.get_account(1)
    print(f"Account 1 now balance={a.balance}")

    print("Deleting account 3")
    repository.delete_account(3)

    print("Final accounts:")
    for a in repository.list_accounts():
        print(f"id={a.id}, owner={a.owner}, balance={a.balance}, type={a.type}")


if __name__ == '__main__':
    main()
