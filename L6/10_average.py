"""

# 10_average.py

yek tabe benevisit ke yek listi az nomarat begire va mianginesh ro hesab kone

ejaze nadarid az tavabe ye dakheli mesle sum() estefade konid.


"""


def average(numbers_list : list ) -> float :
    """
    SUMMARY : tabe made nazar miangin ra mohasebe mikonad.

    Parameters
    ----------
    numbers_list : list
        DESCRIPTION : listi az adad be onvane vorodi entekhab mishavad.

    Returns
    -------
    float
        DESCRIPTION : dar enteha miangin be onvane khoroji bargardande mishavad.
    """
    
    summ = 0
    for numbers in numbers_list :
        summ += numbers
        
    average_numbers = summ / len(numbers_list)
    return average_numbers



check_average = average([20,13,15,18,19,16])
print("your average is :", check_average)


"""
your average is : 16.833333333333332

"""
