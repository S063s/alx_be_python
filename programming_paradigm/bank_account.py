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
    account = BankAccount("250", "John Doe", "123456789")
    account.display_balance()

    print("Depositing $67.0...")
    account.deposit(67.0)
    account.display_balance()

    print("Withdrawing $100.0...")
    account.withdraw(100.0)
    account.display_balance()

    print("Attempting to withdraw $2000...")
    if not account.withdraw(2000.0):
        print("Insufficient funds for this withdrawal.")
    account.display_balance()
   
