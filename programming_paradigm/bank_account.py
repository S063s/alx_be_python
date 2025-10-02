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

    account = BankAccount("123456789", "John Doe", 1000.0)
    account.display_balance()

    print("Depositing $500...")
    account.deposit(500)
    account.display_balance()

    print("Withdrawing $200...")
    account.withdraw(200)
    account.display_balance()

    print("Attempting to withdraw $2000...")
    if not account.withdraw(2000):
        print("Insufficient funds for this withdrawal.")
    account.display_balance()
   