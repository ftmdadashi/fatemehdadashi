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




#-----------------------------------------------------------------------------------------




def name_cleaner(name):
    name2 = name.strip()
    clean_name = name2.title()
    return clean_name
    
    
def name_cleaner(name):
    clean_name = name.strip().title()
    return clean_name

    
  
def name_cleaner(name):
    return name.strip().title()





#-------------------------------------------------------------------------------------------

sentence='ali,payam,mohsen'

sentence.split()#Out[28]: ['ali,payam,mohsen'] inja list yek moalefe dare.

sentence.split(' ')

sentence.split(',') #Out[30]: ['ali', 'payam', 'mohsen'] inja list 3 moalefe dare.





def name_cleaner(name):
    #name.split(' ')
    new_name = name.split() 
    clean_name =new_name[0].title() + ' ' + new_name[1].title()
    return clean_name
    


name_cleaner("   aLi   pILeHvAr     ") #Out[34]: 'Ali Pilehvar'


name_cleaner("   aLi   pILeHvAr  Meibody   ")  #Out[35]: 'Ali Pilehvar'
#rare case --> nader begard

def name_cleaner(name):
    #name.split(' ')
    splitted_name = name.split()
    
    joined_name=' '.join(splitted_name)
    clean_name = joined_name.title()
    return clean_name
    


name_cleaner("   aLi   pILeHvAr     ") #Out[34]: 'Ali Pilehvar'

name_cleaner("   aLi   pILeHvAr  Meibody   ")  # 'Ali Pilehvar Meibody'













