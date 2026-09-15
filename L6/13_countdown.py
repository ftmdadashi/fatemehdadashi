"""

# 13_countdown.py

yek tabe benevisid ke vorodi yek adad begire va az oon adad ta 0 , print kone .

masalan begire 5 --> va print kone

```bsh
5
4
3
2
1
0
``

"""


def countdown(number : int) -> int :
    """
    SUMMARY : tabe baraye shomareshe adad be sorate varone mibashad.

    Parameters
    ----------
    number : int
        DESCRIPTION : yek add be onvan vorodi entekhab mishavad.

    Returns
    -------
    int
        DESCRIPTION :khoroji niz adadi mibashand ke az adade made nazar ta 0
        dar nazar gerefte shode ast.
    """
    for numbers in range(number,-1,-1) :
        print( numbers )
    
 
countdown(12)


"""
12
11
10
9
8
7
6
5
4
3
2
1
0

"""