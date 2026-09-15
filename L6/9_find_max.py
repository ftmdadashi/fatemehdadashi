"""

# 9_find_max.py

yek tabe benvisid ke yek listi az adad begire va bozorgtarin adad ro peyda kone va khoroji bede.

in tabe dar asl kare tabeye dakhelie max() ro anjam mide , pas ejaze nadarid az max() estefade konid .


"""

def find_max(numbers_list : list) -> int :
    """
    SUMMARY : tabe baraye peyda kardane adade max dar yek list mibashad.

    Parameters
    ----------
    numbers_list : list
        DESCRIPTION : yek list az adad be onvane vorodi entekhab mishavad.

    Returns
    -------
    int
        DESCRIPTION : bozorgtarin adad az list be onvane khoroji barmigardad.
    """
    
    max_number = numbers_list[0]
    for numbers in numbers_list :
        if numbers > max_number :
            max_number = numbers
            
    return max_number



find_max_number = find_max([20,40,12,80,35])
print("In your numbers list, the max is :",find_max_number)



"""

In your numbers list, the max is : 80

"""