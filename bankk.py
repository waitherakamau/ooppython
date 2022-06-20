from datetime import datetime


class Account:
    def __init__(self,full_name, number):
        self.full_name =full_name
        self.number =number
        self.account_balance=0
        self.deposits=[] #Add a new attribute to the class Account called deposits which by default is an empty list.
        self.withdraws=[]  #Add another attribute to the class Account called withdrawals which by default is an empty list.
        self.transaction=100
        self.words={}
        self.loan_balance=0
        self.statement=[]
    def deposit(self,amount):
      
        if amount <=0:
             print(f"Deposit must be positive amount")
        else:
            self.account_balance+=amount   
            now= datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"You have deposited"
            }
            self.deposits.append(amount)
            self.statement.append(transaction) 
            print(f"Hello {self.full_name}, your new balance is {self.account_balance} and your deposits are {self.deposits}and your statement is {self.statement}")
    
        return self.words            

    def withdraw(self,amount) :
        if amount+self.transaction_fee > self.loan_balance:
            print(f"Hello {self.full_name}, your balance is {self.account_balance} you can't withdraw {amount}")    
        elif amount <=0:
            print(f"Withdrawal amount must be greater than 0")
        else:    
            self.account_balance-=amount+self.transaction_fee
            now= datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"You have withdrawn "
            }
            self.withdraws.append(amount)
            self.statement.append(transaction)
            print(f"Hello {self.full_name}, your new balance is {self.account_balance} and the withdrawals are {self.statement}")
    def deposit_statements(self):
         for deposit in self.statement:
             print(deposit)
          
    def deposits_statement(self):
        for statements in self.deposits:
            print(statements)
    def withdraws_statement(self):
        for statements in self.withdraws:
            print(statements)

    def current_balance(self):
        return self.account_balance

    def full_Statement(self):
        for transaction in self.statement:
            amount = transaction["amount"]
            Narration= transaction["Narration"]
            time= transaction["time"]
            date= time.strftime("%x/%X")
            print(f"{date}:   {Narration}   {amount}")

    def borrow(self,amount):    
        item = len(self.deposits)
        item_s = sum(self.deposits)
        limit = item_s*(1/3)
        amount+=(amount)*0.03 
       
        if amount<=100:
            return "Sorry we can't give you this loan, your loan must be more than 100 "
        elif self.loan_balance>0:
            return f"Dear customer you still have a loan of {self.loan_balance}"
        elif item<10:
            return f"Your deposits must be atleast 10"

        elif amount>=limit:
            return f"Dear customer you can't borrow {amount}is higher than a limit of {self.loan_balance}"

        else:
            self.loan_balance+=amount
            return f"Dear customer {self.full_name} your loan of ksh{amount} has been granted successfully"

    def loan_repay(self,amount): 
        if amount<self.loan_balance:
            paying = self.loan_balance-amount
            return f"Dear customer you have paid {amount} and your loan balance is {paying}"
        else:
            over_pay = amount-self.loan_balance
            self.loan_balance+=over_pay
            return f"You succesfully completed paying your loan and the over pay is {over_pay} and your new balance is {self.account_balance}"  
   
    def transfer(self,amount,instance_account):
        if amount<=0:
            return f"invalid"
        if amount>= self.account_balance:
            return f"insufficient amount in your account"
        if isinstance(instance_account,Account):
            self.loan_balance-=amount
            instance_account.loan_balance += amount
            return f"you have transfered {amount} to {instance_account} account with the name {instance_account.full_name} and your new balance is {self.account_balance}"

