"""

# 12_calculator.py

yek tabe benvisid ke do adad begire va yek operation

agar operation jam bod anjam bede va javab ro khoroji bede

agar tafrigh --> menha kone bargardon

agar zarb bood --> zarb kone bargardoone

agar taghsim bood --> taghsim kone bargardone

agar operation chizi joz jam,tafrigh,zarb,taghsim bood , None bargardoone


"""


def calculator(number1 : int ,number2 : int ,operation : str) -> int :
    """
    SUMMARY : tabee shabih be mashin hesab baraye mohasebeye amaliate riyazi.

    Parameters
    ----------
    number1 : int
        DESCRIPTION : adade aval be onvane vorodi aval.
    number2 : int
        DESCRIPTION : adade dovom be onvane vorodi dovom.
    operation : str
        DESCRIPTION : amaliat riyazi be onvane vorodi sevom

    Returns
    -------
    int
        DESCRIPTION : khoroji pasokhe amaliate riazi mibashad.
    """
    
    if operation == "jam":
        result = number1 + number2
        return result
    elif operation == "tafrigh":
        result = number1 - number2
        return result
    elif operation == "zarb":
        result = number1 * number2
        return result
    elif operation == "taghsim":
        result = number1 / number2
        return result
    else :
        return None
    
    
 
calculator_result = calculator(35, 7, "taghsim")
print("your result is :", calculator_result)

"""
your result is : 5.0
"""

   
    
calculator_result = calculator(35, 7, " ")
print("your result is :", calculator_result)

"""
your result is : None
"""
     
    
    
    
    
    
    
    
    
    
    
    