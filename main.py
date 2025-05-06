# Apollos Eastman
# 5/6/2025
# Three Ways to Modify BankAccount Class Attributes

class BankAccount():
    ''' A simple bank accouint class'''

    def __init__(self, acc_holder, balance = 0):
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'You deposited ${amount}. Your balance is now ${self.balance}.')
        else:
            print(f'Invalid deposit')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'You withdrew ${amount}. Your balance is now ${self.balance}.')
        else:
            print(f'Invalid withdrawal')

    def get_balance(self):
        return self.balance
    
    def disp_acc_info(self):
        print(f'Account holder: {self.acc_holder}\nBalance: ${self.balance}')

account1 = BankAccount('Apollos Eastman', 1500)

account1.disp_acc_info()
account1.deposit(100)
account1.withdraw(500)
account1.withdraw(2500)

print(f'{account1.acc_holder} has a balance of ${account1.get_balance()}')

print()

account2 = BankAccount('John doe', 6000000000000001)

account2.disp_acc_info()
account2.deposit(5)
account2.withdraw(732163121121)
account2.withdraw(9999999999999122112121121)

print(f'{account2.acc_holder} has a balance of ${account2.get_balance()}')

print()

account3 = BankAccount('Isaac Bissonette', 2)

account3.disp_acc_info()
account3.deposit(0)
account3.withdraw(1)
account3.withdraw(50)

print(f'{account3.acc_holder} has a balance of ${account3.get_balance()}')
