from typing_extensions import Self


class Acount:
     def __init__( self,balance,accountnumber):
         self.balance=balance
         self.accountnumbrer=accountnumber
     def deposit(self,amount):
         self.amount=amount
         self.balance+=amount
         return self.balance
         return f"my deposit{amount} on the account{self.account_number},my balance{self.balance}"
     def withdraw(self,amount):
         self.amount=amount
         self.withdraw-=amount
         return self.amount
         return f"withdraw{amount} on the account{self.account_number},my balance{self.balance}"


