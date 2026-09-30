"""

      project3
      \
      \
      \_________main.py
      \_________config.py
      \
      \_________accounts
      \         \
      \         \_________init.py
      \         \_________account.py
      \         \_________authentication.py
      \
      \
      \_________ payments
                \
                \__________init.py  
                \__________payment.py
                \_________fee.py
          



"""





from config import get_bank_name
from accounts.account import creat_account
from accounts.authentication import login
from payments.payment import make_payment
from payments.fee import calculate_fee


#PS F:\python\8_class\L8\project3> python main.py



















