class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance


class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner, overdraft_limit, balance=0):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Overdraft limit exceeded")

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account):
        self.accounts.remove(account)

    def list_accounts(self):
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Owner: {account.owner}, Balance: {account.balance}")

    def total_funds(self):
        total = sum(account.get_balance() for account in self.accounts)
        print(f"Total funds in the bank: {total}")
        return total

checking = CheckingAccount("CA54321", "Beka", 500, 200)

bank = Bank("MyBank")
bank.add_account(checking)


checking.withdraw(600)
checking.deposit(300)

bank.list_accounts()
bank.total_funds()

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=0):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance + self.overdraft_limit:
            self.balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate / 100

if __name__ == "__main__":
    checking = CheckingAccount("Beka", 1000, 500)
    checking.deposit(500)
    checking.withdraw(200)
    print(checking.balance)

    savings = SavingsAccount("Adilet", 1000, 5)
    savings.deposit(500)
    savings.withdraw(200)
    savings.add_interest()
    print(savings.balance)

