"""

# 14_multiplication_table.py

yek tabe benevisid ke jadval zarb bashe masalan vorodi begire 5 va ino print kone

```bsh
5 × 1 = 5
5 × 2 = 10
...
5 × 10 = 50
`

"""


def multiplication_table(number : int) -> int :
    """
    SUMMARY : tabe jadval zarbe 1 ta 10 yek adade moshakhas.

    Parameters
    ----------
    number : int
        DESCRIPTION : yek adad be onvane vorodi entekhab mishavad.

    Returns
    -------
    int
        DESCRIPTION : khoroji jadval zarbe adade made nazar ast.
    """
    
    for i in range(1,11) :
        multiplication = number * i
        print(number,"*",i,"=",multiplication)
        
        
        

multiplication_table(5)
        

"""

5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50

"""