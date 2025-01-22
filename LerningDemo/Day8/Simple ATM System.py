class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}."

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. Remaining balance: ${self.balance}."
        return "Insufficient funds."

    def check_balance(self):
        return f"Account Balance: ${self.balance}"


# Example usage
account = Account("12345", 100)

print(account.check_balance())
print(account.deposit(50))
print(account.withdraw(30))
print(account.withdraw(200))  # Try withdrawing more than balance
