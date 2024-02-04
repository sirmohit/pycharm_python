class Bank:
    def __init__(self,name,balance = 0):
        self.name = name
        self.balance = balance
    def __str__(self):
        return f"Account holder name : {self.name} \nBalance : {self.balance}"
    def deposit(self,amount):
        self.balance = self.balance+ amount
        print(f"diposited {amount} to your accout")
    def withdraw(self,amount):
        if amount>self.balance:
            print("you do not have sufficient balance")
        else:
            self.balance = self.balance-amount
            print(f"{amount} is withdraw from your account and your current balance is {self.balance}")
obj = Bank("Mohit",2334342)
print(obj)
obj.deposit(2344444)
obj.withdraw(123434)
