class Wallet:
       def __init__(self):
        self.__balance=0

       def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("Invalid Deposit")

       def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
        else:
              print("Invalid Withdraw")

       @property
       def balance(self):
        return self.__balance
    
w=Wallet() 
w.deposit(1000)
w.deposit(500)

print("Balance=",w.balance)

w.withdraw(300)

print("Balance=",w.balance)

    
