"""

2. barresi mojodi mahsoolat.

yek dict az mahsoolat va mojodi anan darim. in dict ra be onavane vorodi yek

tabe dar nazar grefte va do khoroji midahad. do list ke :
    
1. list e mahsoolati ke mojodi darand.
2. list e mahsoolati ke mojodi nadarand.

inventory = {"apple":20,
             "banana":5,
             "orange":0,
             "milk":12,
             "bread": 0} 

"""


#----------------------------------------1-----------------------------------------------


def product_inventory(inventory : dict) -> list :
    """
    SUMMARY : in tabe dar yek dict, name mahsoolati ke mojodi darand ra 
    barmigardanad.

    Parameters
    ----------
    inventory : dict
        DESCRIPTION : tanha vorodi in tabe yek dict az mahsoolat ast.

    Returns
    -------
    list
        DESCRIPTION : khoroji tabe, listi az mahsoolati ast ke mojod mibashand.
    """
    
    
    inventory_list = []
    for name , stock in inventory.items() :
        if stock > 0 :
            inventory_list.append(name)
            
    return inventory_list



 
inventory = {"apple":20,
             "banana":5,
             "orange":0,
             "milk":12,
             "bread": 0} 

check = product_inventory(inventory)
print("These products have stocks =", check)    
#These products have stocks = ['apple', 'banana', 'milk']



#-------------------------------------------2--------------------------------------------

def product_not_inventory(inventory : dict) -> list :
    """
    SUMMARY : in tabe name mahsoolati ke mojodi nadarand ra dar yek list
    barmigardanad.

    Parameters
    ----------
    inventory : dict
        DESCRIPTION : tanha vorodi in tabe yek dict ast.

    Returns
    -------
    list
        DESCRIPTION : tanha khoroji in tabe yek list az name mahsoolati ast
        ke mojodi nadarand.
    """
    
    
    not_inventoy_list = []
    for  name , stock in inventory.items() :
        if stock == 0 :
            not_inventoy_list.append(name)
            
    return not_inventoy_list


        

 
inventory = {"apple":20,
             "banana":5,
             "orange":0,
             "milk":12,
             "bread": 0} 

check = product_not_inventory(inventory)
print("These products have not stocks =", check)   
#These products have not stocks = ['orange', 'bread']   


















   
            