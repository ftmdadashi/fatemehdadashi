"""

# 7_check_password.py

a) yek tabe benevisid ke password ro begire va bayad hadeaghal 8 character , hadeaghal 
yek adad, hadeaghal yek harf dakehelsh bashe  . agar bood faghat print kone 'password sabt shod'
 ,agar nabood print kone 'password kamel nist'


b) hamon tabe ro benevisid ama agar password dorost bod chizi print nakone balke khorojhi 
bede True , dar gheyre insorat khoroji bede False

c) Yek tabe besazid bename check_password_strength ke ghodrate password ro besanje yani 
dar khoroji yek adad bede beyne 1 ta 4 . 

- 4: agar ham bala 8 ragham bod va ham harf dahst ham adad , ham bozorg ham kochak 

- 3 : agar ham bala 8 ragham bod ham harf dahst ham adad dasht 

- 2 : agar bala 8 raghamm bood

- 1 : agar paeine 8 bood 1 bede


"""


#---------------------------------a----------------------------------------------

def check_password(password : str) -> str :
    """
    SUMMARY : dar in tabe bayad password ba tavajoh be mahdodiat haye 
    taeen shode entekhab va ya rad shavad. hatman bayad az print dar tabe
    estefade kard va chon az return dar tabe estefade nmikonim hatman bayad
    dar seda zadan tabe tanha khode tabe ra seda konim bedone inke dar zarfi 
    gozashte shavad, chon dar gheir in soorat dar entehaye khoroji, none niz
    print mishavad.

    Parameters
    ----------
    password : str
        DESCRIPTION : password be onvane vorodi entekhab shode ast.

    Returns
    -------
    str
        DESCRIPTION : dar enteha ba yek jomle be onvane khoroji, vaziiat 
        moshakhas mishavad.
    """
    
    if len(password) >= 8 :
        if  not password.isdigit() and not password.isalpha() :
            print("password sabt shod.")
        else :
            print("password kamel nist.")
    else :
        print("password kamel nist.")
        
        

check_password("fghjjhgfxsaasghj")



"""
password kamel nist.

"""





#---------------------------------b----------------------------------------------

def check_password_bool(password : str) -> bool :
    """
    SUMMARY : dar in tabe bayad password ba tavajoh be mahdodiat haye 
    taeen shode entekhab va ya rad shavad.

    Parameters
    ----------
    password : str
        DESCRIPTION : password be onvane vorodi entekhab shode ast.

    Returns
    -------
    bool
        DESCRIPTION : dar enteha ba True ya False be onvane khoroji, vaziiat 
        moshakhas mishavad.
    """
    
    if len(password) >= 8 :
        if  not password.isdigit() and not password.isalpha() :
            return True
        else :
            return False
    else :
        return False        
        

check = check_password_bool("hgfj1255")
print("your password is :",check)



"""
your password is : True

"""




#---------------------------------c----------------------------------------------

def check_password_strength(password : str) -> int :
    """
    SUMMARY : dar in tabe be password vorodi barasase filterhaye moshakhas
    emtiyaz dade mishavad.

    Parameters
    ----------
    password : str
        DESCRIPTION : password be onvane vorodi dar in tabe mibashad.

    Returns
    -------
    int
        DESCRIPTION : khoroji in tabe adadi ast beyne 1 ta 4 .
            
    """
    
    if len(password) >= 8 :
        if not password.isdigit() and not password.isalpha() :
            if not password.islower() and not password.isupper() :
                return 4
            return 3
        return 2
    return 1



check = check_password_strength("hghhhjhjhjh")
print("your password star is :",check)


"""
your password star is : 2

"""