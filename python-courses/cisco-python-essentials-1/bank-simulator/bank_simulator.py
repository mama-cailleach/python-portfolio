def display_menu():
    print("\nBank Account Menu:")
    print("1. Create new account")
    print("2. Deposit funds")
    print("3. Withdraw funds")
    print("4. View balance")
    print("5. Exit")

def create_account(accounts):
    name = input("Enter account name: ").strip()
    if name in accounts:
        print("Account already exists.")
        return
    while True:
        try:
            balance = float(input("Enter starting balance: "))
            if balance < 0:
                print("Balance cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid amount.")
    accounts[name] = balance
    print(f"Account '{name}' created with balance {balance:.2f}")

def deposit(accounts):
    name = input("Enter account name: ").strip()
    if name not in accounts:
        print("Account not found.")
        return
    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        accounts[name] += amount
        print(f"Deposited {amount:.2f}. New balance: {accounts[name]:.2f}")
    except ValueError:
        print("Please enter a valid amount.")

def withdraw(accounts):
    name = input("Enter account name: ").strip()
    if name not in accounts:
        print("Account not found.")
        return
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        if accounts[name] < amount:
            print("Insufficient funds.")
            return
        accounts[name] -= amount
        print(f"Withdrew {amount:.2f}. New balance: {accounts[name]:.2f}")
    except ValueError:
        print("Please enter a valid amount.")

def view_balance(accounts):
    name = input("Enter account name: ").strip()
    if name in accounts:
        print(f"Account '{name}' balance: {accounts[name]:.2f}")
    else:
        print("Account not found.")

def main():
    accounts = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            view_balance(accounts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
