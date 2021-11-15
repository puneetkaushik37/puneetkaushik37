# Object Oriented Programming Challenge

# For this challenge, create a bank account class that has two attributes:

# * owner
# * balance

# and two methods:

# * deposit
# * withdraw

# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
         
    def deposit(self,credit):
        self.balance += credit
        return "Deposit Accepted"
    
    def withdraw(self,debit):
        if(self.balance < debit):
            return "Not Enough balance"
        else:
            self.balance -= debit
            print("Withdrawal Accepted")
    
    def __str__(self):
        return (f"Account owner: {self.owner}\nAccount balance: {self.balance}") 
    
    
acct1 = Account('Jose',100)
print(acct1)
acct1.owner
acct1.balance
acct1.deposit(50)
acct1.withdraw(75)
# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
    