class Account:
     def get_interest_rate(self):
          return 4

class SavingAccount(Account):
      def get_interest_rate(self):
           return 5.5

class FixedDeposite(Account):
     def get_interest_rate(self):
          return 7.2
          
accounts=[Account(),SavingAccount(),FixedDeposite()]
for acc in accounts:
     print(f"Interest Rate:{acc.get_interest_rate()}%")



