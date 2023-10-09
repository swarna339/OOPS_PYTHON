from abc import ABC, abstractmethod

# Abstract class Account
class Account(ABC):
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # abstractmethod
    def deposit(self, amount):
        pass

    # abstractmethod
    def withdraw(self, amount):
        pass

    def check_balance(self):
        return self.balance

# Subclass SavingsAccount       //polymorphism
class SavingsAccount(Account):    
    def __init__(self, account_number, account_holder, balance, min_balance):
        super().__init__(account_number, account_holder, balance)
        self.min_balance = min_balance

        #   polymorphism
    def deposit(self, amount):             
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Insufficient balance!")

# Subclass CurrentAccount                    //inheritance
class CurrentAccount(Account):    
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    #  polymorphism of deposit
   
    def deposit(self, amount):   
        self.balance += amount

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
        else:
            print("Overdraft limit exceeded!")

# Bank class
class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

# Create instances of accounts
savings_account = SavingsAccount("S123", "John Doe", 5000, 1000)
current_account = CurrentAccount("C456", "Jane Smith", 10000, 2000)

# Create a Bank instance and add accounts
bank = Bank()
bank.add_account(savings_account)
bank.add_account(current_account)

# Perform operations on accounts
savings_account.deposit(2000)
current_account.withdraw(5000)

# Check account balances
print("Savings Account Balance:", savings_account.check_balance())
print("Current Account Balance:", current_account.check_balance())
