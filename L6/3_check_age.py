"""

# 3_check_age.py

yek tabe benevsidi ke vorodi sen ro begire agar sen kamtar az 18 bood , 
'access denied' khoroji bede, dar gheyre insoorat 'Welcome'


"""


#---------------------------------------a------------------------------------------

def check_age(age : int) -> str :
    """
    SUMMARY : tabe dastresi az tarighe mahdodiate seni.

    Parameters
    ----------
    age : int
        DESCRIPTION : vorodi sen mibashad.

    Returns
    -------
    str
        DESCRIPTION : khoroji str mibashad ke dastresi ra moshakhas mikonad.
    """
    
    if age < 18 :
        return "access denied"
    
    else :
        return "welcome"
    
    
your_age = check_age(18)
print("-----",your_age,"------")


"""
----- welcome ------

"""

























