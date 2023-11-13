class Account:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest calculated: ${interest}")


class CheckingAccount(Account):
    def __init__(self, account_number, balance=0.0, overdraft_limit=100.0):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or overdraft limit exceeded.")


def main():
    savings_account = SavingsAccount("SA123", 1000, 0.03)
    savings_account.deposit(500)
    savings_account.withdraw(200)
    savings_account.calculate_interest()

    checking_account = CheckingAccount("CA456", 500, 100)
    checking_account.withdraw(200)
    checking_account.withdraw(600)


if __name__ == "__main__":
    main()
