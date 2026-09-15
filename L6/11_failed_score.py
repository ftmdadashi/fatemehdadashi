"""

# 11_failed_score.py

yek tabe benevisid ke listi az nomre haor begire va nomre haye fail ro hazf
 kone va oon list ro bargardoone

masalan vorodi
```bsh
[18, 7, 13, 9, 20, 5]
``` 

begire va khoroji bede
```bsh
[18, 13, 20]
```

b) halam hamon vorodi yek list begire az nomre ha va khoroji liste onaei ke fail shodan ro pass bede 


c) hala hamon vorodi yek list begire az nomre ha va dar khoroji bejaye list, 
tedade afradi ke pass shodan ro pass bede


"""


#------------------------------------a--------------------------------------------

def failed_score(numbers_list : list) -> list :
    """
    SUMMARY : tabee baraye peyda kardane nomarat pass az tarighe list.

    Parameters
    ----------
    numbers_list : list
        DESCRIPTION : dar in tabe listi az nomarat be onvane vorodi entekhab mishavad.

    Returns
    -------
    list
        DESCRIPTION : dar in tabe liste khoroji shamele nomarate pass shode ast.
    """
    for numbers in numbers_list :
        if numbers < 10 :
            numbers_list.remove(numbers)
            
    return numbers_list


check_numbers = failed_score([10,12,13,9,20])
print("your passed numbers list is :",check_numbers)            


"""
your passed numbers list is : [10, 12, 13, 20]

"""




#------------------------------------b--------------------------------------------

def failed_score_list(numbers_list : list) -> list :
    """
    SUMMARY : dar in tabe nomarat fail az list hazf shode va dar list digari
    rikhte mishavad..

    Parameters
    ----------
    numbers_list : list
        DESCRIPTION : dar in tabe listi az nomarat be onvane vorodi entekhab mishavad.

    Returns
    -------
    list
        DESCRIPTION : listi az nomarate fail shode dar khoroji namayesh dade mishavad..
    """
    failed_list = []
    for numbers in numbers_list :
        if numbers < 10 :
            numbers_list.remove(numbers)
            failed_list.append(numbers)
            
    return failed_list


check_numbers = failed_score_list([10,1,13,9,20])
print("your failed numbers list is :",check_numbers)            


"""
your failed numbers list is : [1, 9]

"""




#------------------------------------c--------------------------------------------

def failed_score_number(numbers_list : list) -> int :
    """
    SUMMARY : tabee baraye peya kardane tedad afrade pass shode mibashad..

    Parameters
    ----------
    numbers_list : list
        DESCRIPTION : dar in tabe listi az nomarat be onvane vorodi entekhab mishavad.

    Returns
    -------
    list
        DESCRIPTION : tedad afrad pass shode faghat ba yek adad namayesh dade mishavad..
    """
    count = 0
    for numbers in numbers_list :
        if numbers >= 10 :
            count += 1
              
    return count


check_numbers = failed_score_number([10,1,13,9,20])
print("the numbers of passed is :",check_numbers)            



"""
the numbers of passed is : 3
"""







































