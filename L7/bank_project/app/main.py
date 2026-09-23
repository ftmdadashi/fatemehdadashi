"""

5. kar ba package.

yek package be name bank_project besazid.

    bank_package
    |
    |________bank
             |
             |______account.py
             |______fees.py
             |
             |_____app
                   |
                   |_______main.py
                   |_______calculator.py
                   
                   
                   
                   
1. dakhele account.py yek tabe be name show_balance(balance) benevisid ke yek

vorodi daryaft konad, aan ra dar 100 zarb konad va bargardanad.

2. dar calculator.py yek yek tabe be name deposit(balance,amount) benevisid ke 

meghdar amount ra be balance ezafe konad.

3. dar file fees.py yek tabe be name apply_fee(balance,fee) benevisid ke meghdar

fee ra az balance kam konad va natije ra bargardanad.

4. dar main.py bayad yek script benevisid ke chizi shabih be in bashad.

balance = 1000
print(show_balance(balance))
balance = deposit(balance, 500)
print(show_balance(balance))
balance = apply_fee(balance, 50)
print(show_balance(balance))

"""

from ..bank.account import show_balance
from .calculator import deposit
from ..bank.fees import apply_fee



balance = 1000
print(show_balance(balance))

balance = deposit(balance, 500)
print(show_balance(balance))

balance = apply_fee(balance, 50)
print(show_balance(balance))

#ba run kardan dar spyder : ImportError: attempted relative import with no known parent package
#banabar in dar powershell file ra be soorate yek moudle az parent(bank_package)
#run mikonim.
#PS F:\python\7_class\L7> python -m bank_project.app.main
#100000
#150000
#145000
























