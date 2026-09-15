"""

# 15_check_stock.py

yek tabe benevisid ke do vorid begire, yeki dictionary az mahsoolat va yeki esme mahsool

masalan

```python
products = {
    "iphone": 5,
    "macbook": 2,
    "airpods": 0
}
```

va 

```bsh
iphone
```

va dar khoroji agar mojodi 0 nabashe True bede, agar na False bede

"""


def check_stock(product_dict : dict , product : str ) -> bool :
    """
    SUMMARY : tabee baraye vojode yk kala bar asase mojodi tarif shode.

    Parameters
    ----------
    product_dict : dict
        DESCRIPTION : yek dict az mahsolat be hamrah mojodi anan ba onvan vorodi
        dar nazar gerefte mishavad.
    product : str
        DESCRIPTION : esme mahsoli ke ghasd darim mojodi aan ra check konim 
        be onvan vorodi dar nazar gerefte mishavad.

    Returns
    -------
    bool
        DESCRIPTION : True va ya False be onvane khoroji bargardande mishavad.
    """
    
    for name,numbers in product_dict.items() :
        if name == product:
            if numbers != 0 :
                return True
            return False
        
        
check = check_stock({"iphone": 5,"macbook": 2,"airpods": 0},"airpods")
print(check)
            
"""
False
"""
            
            
            
check = check_stock({"iphone": 5,"macbook": 2,"airpods": 0},"iphone")
print(check)


"""
True
"""
