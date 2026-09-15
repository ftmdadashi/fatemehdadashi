"""

# 5_name_cleaner.py

yek tabe benevisid ke esme kamel (esm famil) ro begire va dorostesh kone kamel va khoroji bede

```bsh
"   aLi   pILeHvAr     "
```

va khroji bayad in bashe

```bsh
"Ali Pilehvar Meibody"
```

"""


def name_cleaner(fullname : str ) -> str :
    """
    SUMMARY : tabe moratab kardane name.

    Parameters
    ----------
    fullname : str
        DESCRIPTION : fullname be onvane vorodi.

    Returns
    -------
    str
        DESCRIPTION : fullname be sorate moratab shode be onvan khoroji.
    """
    
    new_fullname = fullname.strip().title()
    return new_fullname


new_clean_full_name = name_cleaner("fatEMEh DADAshI    ")
print("your clean name is :",new_clean_full_name)


"""

your clean name is : Fatemeh Dadashi

"""