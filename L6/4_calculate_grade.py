"""

# 4_calculate_grade.py

yek tabe benevisid ke systeme nomre dehi hast , va nomre beyne 0 ta 100 begire va dar java ino bargardoone

```bsh
90-100 -> A
80-89 -> B
70-79 -> C
60-69 -> D
below 60 -> F

"""

def calculate_grade(number:float) -> str :
    """
    SUMMARY : tabe tashkhise grade az tarighe nomre.

    Parameters
    ----------
    number : float
        DESCRIPTION : nomre be onvan vorodi dar nazar gerefte mishavad.

    Returns
    -------
    str
        DESCRIPTION : grade az type str be onvane khoroji mibashad.
    """
    
    if number > 100 or number < 0 :
        raise ValueError ('nemishavad balaye 100 ya zire sefr bshad')
    
    elif number >= 90 :
        return "A"
    
    elif number >= 80 :
        return "B"
    
    elif number >= 70 :
        return "C"
    
    elif number >= 60 :
        return "D"
    
    else :
        return "F"
    
    
    

grade = calculate_grade(-2)
print("your grade is :",grade)


"""
your grade is : None

"""


