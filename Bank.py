class Account:
    def __init__(self,name,number):
        self.name=name
        self.number=number
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
        return f"Hello {self.name}you have deposited {amount}your new balance is{self.balance}


