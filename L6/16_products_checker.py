"""

# 16_products_checker.py


yek list az mahsolat darim ke har mahsool yek dictionary hast mesle 

```python
products=[ {'code':'z1' , 'name' :'zara cloth 121' ,'price':30},
          {'code':'z2' , 'name' :'zara shooes 100' ,'price':45},
          {'code':'z3' , 'name' :'zara cloth 451' ,'price':35},
          {'code':'z4' , 'name' :'zara shooes 300' ,'price':55},
          {'code':'z5' , 'name' :'zara shooes 231' ,'price':60},
          {'code':'z6' , 'name' :'zara bag 400' ,'price':110},
          {'code':'z7' , 'name' :'zara bag 500' ,'price':95}]
```

a) vorodie tabe yeki products ro begrie va yeki code e mahsol va dar khoroji gheymat ro pas bede


b) vorodi products begire va code e mahsol va name mahsool ro bargardoone 


c) vorodi products begire va code mahsool va khoroji yek tuple begire injori:

(z7,zara bag 500 ,  95)


"""


#------------------------------------a---------------------------------------------


def products_checker(product_list : list , product_code : str) -> int :
    """
    SUMMARY : tabe peyda kardan gheymat mahsol ba estefade az code aan dar yek list
    e shamele chandin dict ast.

    Parameters
    ----------
    product_list : list
        DESCRIPTION :yek list az mahsolat b onvan vorodi dar nazar gerefte mishavad.
    product_code : str
        DESCRIPTION : code mahsool niz be onvan vorodi dar nazar gerefte mishavad.

    Returns
    -------
    int
        DESCRIPTION : gheymat mahsool be onvane khoroji bargardande mishavad.
    """
    for produtc in product_list :
        if produtc["code"] == product_code :
            return produtc["price"]
        
        



products=[ {'code':'z1' , 'name' :'zara cloth 121' ,'price':30},
          {'code':'z2' , 'name' :'zara shooes 100' ,'price':45},
          {'code':'z3' , 'name' :'zara cloth 451' ,'price':35},
          {'code':'z4' , 'name' :'zara shooes 300' ,'price':55},
          {'code':'z5' , 'name' :'zara shooes 231' ,'price':60},
          {'code':'z6' , 'name' :'zara bag 400' ,'price':110},
          {'code':'z7' , 'name' :'zara bag 500' ,'price':95}]
       
check = products_checker(products, "z1")   
print(check)   
        
        
"""
30
"""
        
        
        
#------------------------------------b---------------------------------------------


def product_checker_list(products_list : list) -> str :
    """
    SUMMARY : dar in tabe bayad name va code mahsool bargardande shavad.

    Parameters
    ----------
    products_list : list
        DESCRIPTION : list mahsoolat be onavane vorodi dar nazar gerefte mishavad.

    Returns
    -------
    str
        DESCRIPTION : name va code bargardande mishavand.
    """
    
    for product in products_list :
        return product["name"] , product["code"]
        
        
        
        
  

products=[ {'code':'z1' , 'name' :'zara cloth 121' ,'price':30},
          {'code':'z2' , 'name' :'zara shooes 100' ,'price':45},
          {'code':'z3' , 'name' :'zara cloth 451' ,'price':35},
          {'code':'z4' , 'name' :'zara shooes 300' ,'price':55},
          {'code':'z5' , 'name' :'zara shooes 231' ,'price':60},
          {'code':'z6' , 'name' :'zara bag 400' ,'price':110},
          {'code':'z7' , 'name' :'zara bag 500' ,'price':95}]
       
check = product_checker_list(products)   
print(check)   
      
        
      
        
#--------------------------------------c------------------------------------------


def products_checker_tuple(product_list : list , product_code : str) -> tuple :
    """
    SUMMARY :  in tabe etelaate mahsool ra barmigardanad. 

    Parameters
    ----------
    product_list : list
        DESCRIPTION :yek list az mahsolat be onvane vorodi
    product_code : str
        DESCRIPTION : code mahsool be onvane voorodi.

    Returns
    -------
    tuple
        DESCRIPTION : etelaate mahsool be onvane khoroji bargardande mishavad.
    """
    
    for product in product_list :
        if product["code"] == product_code :
            return product["code"] , product["name"] , product["price"]
        
        



products=[ {'code':'z1' , 'name' :'zara cloth 121' ,'price':30},
          {'code':'z2' , 'name' :'zara shooes 100' ,'price':45},
          {'code':'z3' , 'name' :'zara cloth 451' ,'price':35},
          {'code':'z4' , 'name' :'zara shooes 300' ,'price':55},
          {'code':'z5' , 'name' :'zara shooes 231' ,'price':60},
          {'code':'z6' , 'name' :'zara bag 400' ,'price':110},
          {'code':'z7' , 'name' :'zara bag 500' ,'price':95}]
       
check = products_checker_tuple(products, "z1")   
print(check)   
      
        
"""
('z1', 'zara cloth 121', 30)
"""



def find_tuple_by_code(products,code):
    for product in products:
        if product['code']==code:
            product_tuple = (product['code'],product['name'],product['price'])
            return product_tuple


find_tuple_by_code(products,'z3') #Out[81]: ('z3', 'zara cloth 451', 35)



















