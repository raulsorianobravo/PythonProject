class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance-amount

    def deposit(self, amount):
        self.balance = self.balance+amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))
            file.close()

        

# account = Account("./Section26/balance.txt")
# print(account)    
# print(account.balance)  

# account.withdraw(43)
# print(account.balance) 
# account.deposit(443)
# print(account.balance) 

# account.commit()


#inherit
class Checking(Account):
    """ This class generates checking account objects"""

    type="checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount
        self.type = self.balance

    def transferWithFee(self, amount):
        self.balance = self.balance - amount - self.fee



checking = Checking("./Section26/balance.txt", 2)
print(checking)    
print(checking.balance)

checking.deposit(443)
print(checking.balance) 

checking.transfer(410)
print(checking.balance)

print(checking.type)


checking2 = Checking("./Section26/balance.txt", 2)
print(checking2)    
print(checking2.balance)

checking2.deposit(3)
print(checking2.balance) 

checking2.transfer(24)
print(checking2.balance) 
print(checking2.type)

print(checking2.__doc__)