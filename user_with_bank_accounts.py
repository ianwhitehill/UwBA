class BankAccount:

    def __init__(self, int_rate =  0.02, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance < amount:
            self.balance = (self.balance - amount) - 5
            return print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance -= amount
    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
    def display_account_info(cls):
        return print(f"Balance: {cls.balance}")

class User:
    bank_name = "First National Dojo"
    
    def __init__(self, name, email_address, int_rate, balance):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate, balance)
    def make_deposit(self, amount):
        self.account.deposit(amount)
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
    def display_user_balance(self):
        self.account.display_account_info()
    def accrued_interest(self):
        self.account.yield_interest()



guido = User("Guido van Rossum", "guido@python.com", 0.05, 80)
# monty = User("Monty Python", "monty@python.com")
# print(guido.name)	# output: Guido van Rossum
# print(monty.name)	# output: Monty Python

# guido.make_deposit(100)
# guido.make_deposit(200)
# monty.make_deposit(50)
# print(guido.account_balance)	# output: 300
# print(monty.account_balance)	# output: 50

guido.make_deposit(100)
guido.accrued_interest()
guido.make_withdraw(50)
guido.account.display_account_info()


