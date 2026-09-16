"""

# 19_online_store.py

ma yek foroshgahe koochak darim hamchin chizi 

```python
products = [
    {"code": "p1", "name": "Keyboard", "price": 50, "stock": 4},
    {"code": "p2", "name": "Mouse", "price": 30, "stock": 7},
    {"code": "p3", "name": "Monitor", "price": 250, "stock": 2},
    {"code": "p4", "name": "Headphone", "price": 80, "stock": 0}
]
```


a ) tabe ei benevisid ke 

```python
find_product(products, code)
```

code mahsool ro begire agar peyda kard , dictionary mahsol ro bargardone, age peyda nakard None 
pass bede



b) tabe ei benevisid ke yek list bename cart begire :


cart=[]


```python
add_to_cart(products, cart, code)
```

va sepas oon code agar vojod dasht va stock>0 bodo be cart ezafe kone va khoroji cart ro pas bede


c) hamon tabeye (b) ro benevisid ama agar vojod dasht , az products stock ro yedone kam kone va liuste products ro pass bede

d[advanced] ) hamon soale ghabli hast , ama ham be cart ezafe kone , ham products ro ok kone va joftesho pas bede (yani do ta khoroji)

"""



#--------------------------------------------a-----------------------------------

def find_product(products : list, code : str) :
    """
    SUMMARY : tabee baraye peyda kardane telaate yek mahsool bar asase code aan
    mahsool.

    Parameters
    ----------
    products : list
        DESCRIPTION : vorodi yek list az mahsoolat ast.
    code : str
        DESCRIPTION : vorodi dovom code mibashad.

    Returns
    -------
    product : TYPE
        DESCRIPTION : khoroji dar soorate peyda shodane mahsool, etelaat aan
        mahsool va dar gheir in soorat, None mibashad.
    """

    for product in products :
        if product["code"] == code :
            return product
        
        
    return None
            
    


products = [
    {"code": "p1", "name": "Keyboard", "price": 50, "stock": 4},
    {"code": "p2", "name": "Mouse", "price": 30, "stock": 7},
    {"code": "p3", "name": "Monitor", "price": 250, "stock": 2},
    {"code": "p4", "name": "Headphone", "price": 80, "stock": 0}]

check = find_product(products, "p5")
print(check)


"""
None

"""


check = find_product(products, "p2")
print(check)


"""
{'code': 'p2', 'name': 'Mouse', 'price': 30, 'stock': 7}
"""


#--------------------------------------b-----------------------------------------

def add_to_cart(products : list, cart : list, code : str) -> list :
    """
    SUMMARY :ezafe kardane yek mahsool bar asase code aan be yel list khali.

    Parameters
    ----------
    products : list
        DESCRIPTION : vorodi aval ke yek list ast.
    cart : list
        DESCRIPTION : vorodi dovom ke yek list ast.
    code : str
        DESCRIPTION : vorodi sevom ke code mahsool ast.

    Returns
    -------
    list
        DESCRIPTION : khoroji yek list az mahsool made nazar ast.
    """
    

    for product in products :
        if product["code"] == code and product["stock"] > 0 :
            cart.append(product)
            
    return cart
 

cart = []
products = [
    {"code": "p1", "name": "Keyboard", "price": 50, "stock": 4},
    {"code": "p2", "name": "Mouse", "price": 30, "stock": 7},
    {"code": "p3", "name": "Monitor", "price": 250, "stock": 2},
    {"code": "p4", "name": "Headphone", "price": 80, "stock": 0}]

check = add_to_cart(products, cart, "p2")
print(check)



"""
[{'code': 'p2', 'name': 'Mouse', 'price': 30, 'stock': 7}]

"""



#-------------------------------------c-----------------------------------------



def add_to_cart_remove(products : list, code : str) -> list:
    """
    SUMMARY : bad az peyda kardane mahsool bar asase code aan, az stock yeki
    kam shode va products mojadad barmigardad.

    Parameters
    ----------
    products : list
        DESCRIPTION : vorodi aval ke yek list ast.
    code : str
        DESCRIPTION : vorodi dovom ke code mahsool ast.

    Returns
    -------
    list
        DESCRIPTION : khoroji list update shode az mahsoolat ast.
    """
    

    for product in products :
        if product["code"] == code and product["stock"] > 0 :
            product["stock"] = product["stock"] - 1
            return products   
    
    
 

products = [
    {"code": "p1", "name": "Keyboard", "price": 50, "stock": 4},
    {"code": "p2", "name": "Mouse", "price": 30, "stock": 7},
    {"code": "p3", "name": "Monitor", "price": 250, "stock": 2},
    {"code": "p4", "name": "Headphone", "price": 80, "stock": 0}]

check = add_to_cart_remove(products,"p2")
print(check)


"""
[{'code': 'p1', 'name': 'Keyboard', 'price': 50, 'stock': 4},
 {'code': 'p2', 'name': 'Mouse', 'price': 30, 'stock': 6},
 {'code': 'p3', 'name': 'Monitor', 'price': 250, 'stock': 2},
 {'code': 'p4', 'name': 'Headphone', 'price': 80, 'stock': 0}]
"""



#---------------------------------------d-----------------------------------------



def add_to_cart_add(products : list, cart : list , code : str) -> list:
    """
    SUMMARY : bad az peyda shodane mahsoole made nazar, ham products be 
    sorate update shod va ham cart bargardande mishavad.

    Parameters
    ----------
    products : list
        DESCRIPTION : vorodi aval.
    cart : list
        DESCRIPTION : vorodi dovom.
    code : str
        DESCRIPTION : vorodi sevom.

    Returns
    -------
    list
        DESCRIPTION : products va cart be onvane khoroji bargardande mishavand.
    """
    
    
    for product in products :
        if product["code"] == code and product["stock"] > 0 :
            cart.append(product)
            product["stock"] = product["stock"] - 1
            return products , cart 
    
    
 
cart = []
products = [
    {"code": "p1", "name": "Keyboard", "price": 50, "stock": 4},
    {"code": "p2", "name": "Mouse", "price": 30, "stock": 7},
    {"code": "p3", "name": "Monitor", "price": 250, "stock": 2},
    {"code": "p4", "name": "Headphone", "price": 80, "stock": 0}]

check = add_to_cart_add(products,cart,"p3")
print(check)


"""
([{'code': 'p1', 'name': 'Keyboard', 'price': 50, 'stock': 4}, 
  {'code': 'p2', 'name': 'Mouse', 'price': 30, 'stock': 7}, 
  {'code': 'p3', 'name': 'Monitor', 'price': 250, 'stock': 1},
  {'code': 'p4', 'name': 'Headphone', 'price': 80, 'stock': 0}],
 [{'code': 'p3', 'name': 'Monitor', 'price': 250, 'stock': 1}])

"""

