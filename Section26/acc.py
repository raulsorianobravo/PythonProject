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

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount

    def transferWithFee(self, amount):
        self.balance = self.balance - amount - self.fee


checking = Checking("./Section26/balance.txt", 2)
print(checking)    
print(checking.balance)

checking.deposit(443)
print(checking.balance) 

checking.transfer(443)
print(checking.balance) 
