class Acount:
     def __init__( self,account_name,account_number):
         self.balance=0
         self.account_name=account_name
         self.account_numbrer=account_number
         self.deposits=[]
         self.withdrawals=[]
     def deposit(self,amount):
      
        if amount<=0:
            return f"Deposit must be greater than zero"
        
        else:
            self.balance+=amount
            self.deposits.append(amount)
            return f" you have deposited {amount}. your new balance is {self.balance}",self.deposits

        
     def withdraw(self,amount):
        if amount > self.balance:
            return f"your balance is {self.balance}, you cannot withdraw your balance is insuficient {amount}"

            
        elif amount<=0:
            return f"Amount must be greater than zero"
        else:
            self.balance-=amount
            self.deposits.append(amount)

            return f"Hello {self.account_name}you have withdrawn{amount} your new balance is{self.balance}"
     def deposits_statements(self):
          print(*self.deposits,sep="\n")

     def withdrawals_statements(self):
        for withdraw in self.withdrawals:
            return f"you have withdrwan {withdraw} and your balance is {self.withdrawals}"  
            print(*self.withdrawals,sep="\n")    


