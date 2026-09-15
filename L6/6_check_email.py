"""

# 6_check_email.py

yek tabe benvisid ke email ro begire va check kone ke email hast ya na.

chijori mifahmim? bayad fasele beynesh nabashe, bayad @ dashte bashe bayad .com dashte bashe .

agar email bood bayad **True** pass bede agar na **False** pas bede


"""


def check_email(email : str) -> bool :
    """
    SUMMARY : tabe check kardane email az nazare sakhtar.

    Parameters
    ----------
    email : str
        DESCRIPTION : email ba type str be onvane vorodi mibashad.

    Returns
    -------
    bool
        DESCRIPTION : boolean be onvane khoroji tabe mibashad.
    """
    
    if ".com" in email :
        if "@" in email :
            if " " not in email :
                return True
            
            else:
                return False
        else :
            return False
            
    else :
        return False
    
    
    
check = check_email("fdadashigmail.com")
print("your email is :",check)
    


"""

your email is : False

"""