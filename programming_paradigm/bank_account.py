class BankAccount:
    def __init__(self , initial_balance, account_holder, account_number, display_balance=0.0):
        self.initial_balance = initial_balance
        self.account_holder = account_holder
        self.account_number = account_number
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
    account = BankAccount(250.0, "John Doe", "123456789")
    print(f"Account Holder: {account.account_holder}")
    print(f"Account Number: {account.account_number}")
    print(f"Initial Balance: {account.initial_balance}")

    if account.deposit(67.0):
        print(f"Balance after deposit: {account.display_balance}")
        account.display_balance()
    else:
        print("Deposit failed.")

    if account.withdraw(100.0):
        print(f"Balance after withdrawal: {account.display_balance}")
        account.display_balance()
    else:
        print("Withdrawal failed.")

    if account.withdraw(500.0):
        print(f"Balance after withdrawal: {account.display_balance}")
        account.display_balance()
    else:
        print("Withdrawal failed.")
