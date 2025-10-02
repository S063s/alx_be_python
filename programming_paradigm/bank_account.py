class BankAccount:
    def __init__(self, account_number, account_holder, display_balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.display_balance = display_balance

    def deposit(self, amount):
        if amount > 0:
            self.display_balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.display_balance:
            self.display_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: {self.display_balance}")

   
def main():
    import sys
    account = BankAccount(100)
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()