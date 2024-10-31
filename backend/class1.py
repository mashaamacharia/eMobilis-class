class Account:
    def __init__(self,full_name,number,phone,balance):
        self.full_name= full_name
        self.number = number
        self.phone = phone
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Amount ${amount} deposited successfully to account ${self.number}")

    def withdraw(self,amount):
        if self.balance <amount:
            print(f"Insufficient funds. Your balance is ${self.balance} ")
        else:
            self.balance-=amount
            print(f"Amount ${amount} Withdrawn successfully from ${self.number}")
    def check_balance(self):
        print(f"Balance for account ${self.number} is: {self.balance}")

Nesh_acc = Account("Mashaa Macharia","0006","070690878",5000)
Monyangi_acc = Account("Grace Monyangi","0016","070690478",4000)
Nesh_acc.deposit(2000)
Nesh_acc.check_balance()