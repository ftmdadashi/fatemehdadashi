"""

# 2_check_number.py

yek file besazid va tabe(fucntion) haye zir ro besazid

a) tabe bayad vorodi number ro begire , agar zoj bood khoroji bede 'Even' agar fard bood  bede 'Odd'

b) tabe yek vorodi number begire agar zoj bod True bde agar fard bood False pas bede

c) yek tabe benevisid number begire va check kone agar mosbat bood 'Positive' agar manfi 
bood 'Negative' agar sefr bood 'Zero' pas bede


"""



#-----------------------------------------a-----------------------------------------

def check_even_odd(number:int) -> str :
    """
    SUMMARY : tabe tashkhise zoj ya fard bodan.

    Parameters
    ----------
    number : int
        DESCRIPTION : vorodi 

    Returns
    -------
    str
        DESCRIPTION : even ya odd be onvane khoroji.
    """
    
    if number % 2 == 0 :
        return "Even"
    else :
        return "Odd"
    
    
check_number = check_even_odd(13)
print("your number is :",check_number)



"""

your number is : Odd

"""




#-----------------------------------------b-----------------------------------------

def check_even_odd_boolean(number:int) -> bool :
    """
    SUMMARY : tabe tashkhise zoj ya fard bodan.

    Parameters
    ----------
    number : int
        DESCRIPTION : vorodi 

    Returns
    -------
    str
        DESCRIPTION : True ya False be onvane khoroji.
    """
    
    if number % 2 == 0 :
        return True
    else :
        return False
    
    
check_number = check_even_odd_boolean(12)
print("your number is :",check_number)



"""
your number is : True
 
"""



#-----------------------------------------c-----------------------------------------


def check_number_polarity(number:int) -> str :
    """
    SUMMARY : tabe tashkhise polarity.

    Parameters
    ----------
    number : int
        DESCRIPTION : yek adad be onvane vorodi.

    Returns
    -------
    str
        DESCRIPTION : str be onvane khoroji mibashad.
    """
    
    if number > 0 :
        return "positive"
    
    elif number < 0 :
        return "negative"
    
    else :
        return "zero"
    
    
check_number = check_number_polarity(-12)
print("your number polarity is :",check_number)


"""
your number polarity is : negative

"""


































