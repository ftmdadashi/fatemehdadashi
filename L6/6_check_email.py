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

#------------------------------------------------

def check_email(email) :
    shart1 = "@" in email
    sharte2 = "." in email
    sharte3 = " " in email
    
    #har 3 shart bayad True bashad
    all_shart = [shart1,sharte2,sharte3]
    
    if all(all_shart) :
        return True
    else :
        return False
    
    
    
#all--------[True,True,True]
# dar all hameye shartha bayad dorost bashad
#ta all , True beshavad.


#any----------[True,False,False]
#hadeaghal yeki True bashad ok.

#-----------------------------------------------------

#----------
def check_email(email):
    
    #dorahi haye to dar too 
    #na if haye to dar to
    if '@' not in email:
        return False
    elif '.com' not in email:
        return False
    elif ' ' in email:
        return False
    else:
        return True


#-------- if haye jodagane + counting

def check_email(email):
    error_count=0
    

    if '@' not in email:
        error_count = error_count + 1
    
    if '.com' not in email:
        error_count = error_count + 1
        
    if ' ' in email:
        error_count = error_count + 1

    if error_count==0:
        return True
    else:
        return False
        


def check_email(email):
    pass_count=0
    
    if '@'  in email:
        pass_count = pass_count + 1
    
    if '.com'  in email:
        pass_count = pass_count + 1
        
    if ' ' not in email:
        pass_count = pass_count + 1

    if pass_count==3:
        return True
    else:
        return False



#-------
all()
any()


a=[True,True,False,True]

all(a) #Out[41]: False

#tabeye all yechizie -->ya true mide ya false
#age hame azaye list True bashan --> true


a=[True,True,False,True]
b= [True,True,True,True]
c = [True,False,False,False]
d = [False, False, False, False]

all(a) #fALSE --> hame true nisan
all(b) #True ->ham true
all(c) #fasle
all(d) #false


#any --> agr hadeghal yekishon True bashe
any(a) #true
any(b) #true
any(c) #true
any(d) #False


def check_email(email):
    shart1 = '@' in email
    shart2 = '.com' in email
    shart3 = ' ' not in email
    
    #har se ta shart bayad true bashe
    all_shart = [shart1,shart2,shart3]
    
    if all(all_shart):
        return True
    else:
        return False
        
    

def check_email(email):
    shart1 = '@' not in email
    shart2 = '.com' not in email
    shart3 = ' ' in email
    
    #har se ta shart bayad true bashe
    all_shart = [shart1,shart2,shart3]
    
    if any(all_shart):
        return False
    else:
        return True
    







