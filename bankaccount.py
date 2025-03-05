class BankAccount:
    """A simple bank account class"""
    
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def __str__(self):
        """Return account details"""
        return f"BankAccount(owner='{self.owner}', balance=${self.balance:.2f})"

# Example Usage
if __name__ == "__main__":
    try:
        account1 = BankAccount("Alice", 500)
        print(account1)

        account1.deposit(200)
        account1.withdraw(100)
        account1.withdraw(700)  # This should print an insufficient funds message

        # Creating multiple accounts using list comprehension
        accounts = [BankAccount(f"User{i}", balance=i * 100) for i in range(1, 4)]
        for acc in accounts:
            print(acc)
    except Exception as e:
        print(f"An error occurred: {e}")

