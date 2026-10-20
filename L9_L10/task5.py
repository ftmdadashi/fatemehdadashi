"""

yek system banki sadeh tarahi konid ke karbaran betavanand hesab ijad konand,

mojoodi khod ra afzayesh dahand, bardasht anjam dahand va bein hesabhaye mokhtalef pool 

enteghal dahand. class asli bayad BankAcoount name dashte bashad.

vizhegihaye har hesab :
    
owner
account_number
balance
transactions

methodhaye mored niyaz :
    
1. __init__() ijad hesab ba moshakhasate avaliyeh.
2. __str__() namayeshe etelaate hesab.
3. deposit() variz mablagh be hesab.
4. withdraw() bardasht vajh ba baresi mojoodi.
5. transfer() enteghale pool be yek sheye digar az class BankAccount.
6. get_balance() namayeshe mojoodi feli.
7. transactions_history() namayesh tarikhche varizha, bardashtha va enteghalha.

nemone estefade :
    
ali = BankAccount("Ali", "1001", 5000000)
sara = BankAccount("Sara", "1002", 2000000)
 
ali.deposit(1000000)
ali.withdraw(500000)
 
ali.transfer(sara, 2000000)
 
print(ali)
print(sara)
 
ali.transaction_history()

Ghavanin: Mablaghe variz, bardasht va enteghal bayad mosbat bashad. Bardasht
bishtar az mojoodi mojaz nist. Enteghale namovafagh nabayad mojoodi hich hesab
ra taghir dahad. Shomare hesab-ha nabayad tekrari bashand.

#----------------------------chalesh---------------------------------------------

Classe digari be name Bank ijad konid ke tamam hesab-ha ra dar yek list negahdari 
konad va emkanate ijad hesab, jostojooye hesab va namayeshe majmooe mojoodi bank
ra faraham konad.

"""

class BankAccount :
    
     account_list = []
     def __init__(self,owner,account_number,balance) :
         
         if account_number in BankAccount.account_list :
             raise ValueError("account number is available.")
             
         BankAccount.account_list.append(account_number)
         self.owner = owner
         self.account_number = account_number
         self.balance = balance
         self.transactions_list = []
         
         
     def __str__(self) :
         return f"Dear{self.owner} with account number:{self.account_number} your balance is:{self.balance} "
          


     def deposit(self,amount) :
         if amount <= 0 :
             raise ValueError("amount can't be zero or negative.")
             
         else :
             self.balance += amount
             self.transactions_list.append(f"+{amount}")
             print("bamoafaghiat anjam shod")
             print(f"+{amount} variz shod.")
             
     
     def withdraw(self,amount) :
         if amount > self.balance :
             raise ValueError("amount can't be more than balance")
             
         elif amount <= 0 :
             raise ValueError("amount can't be negative.")
             
         else :
             self.balance -= amount
             self.transactions_list.append(f"-{amount}")
             print("bamoafaghiat anjam shod")
             print(f"-{amount} bardasht shod.")
     
             
     def transfer(self, account, amount):
        if amount <= 0:
            raise ValueError("amount can't be negative.")
    
        elif amount > self.balance:
            raise ValueError("amount can't be more than balance.")
        
        else :
            self.balance -= amount
            account.balance += amount
            
            self.transactions_list.append(f"-{amount} transfer to account {account.owner}")
            self.transactions_list.append(f"+{amount} recieve from account {self.owner}")

            print(f"+{amount} tranfer to account {account.owner}")

        
     def get_balance(self) :
         print(f"your balanc is :{self.balance}")
         
         
     def transaction_history(self) :
         for transact in self.transactions_list :
             print(transact)
         
             
             
ali = BankAccount("Ali", "1001", 5000000)
sara = BankAccount("Sara", "1002", 2000000)
 
ali.deposit(1000000)
"""
bamoafaghiat anjam shod
+1000000 variz shod.
"""

ali.withdraw(500000)
"""
bamoafaghiat anjam shod
-500000 bardasht shod.
"""
 
ali.transfer(sara, 2000000)   #+2000000 tranfer to account Sara
 
print(ali)   #DearAli with account number:1001 your balance is:3500000 
print(sara)  #DearSara with account number:1002 your balance is:4000000 
 
ali.transaction_history()

"""
+1000000
-500000
-2000000 transfer to account Sara
+2000000 recieve from account Ali
"""
     
                         
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             












































