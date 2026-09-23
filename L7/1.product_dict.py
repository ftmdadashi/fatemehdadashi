"""

1. kar ba dictionary mahsoolat.

yek dictionary az mahsoolat darim : products = {"laptop" : 1200,
                                                "phone" : 800 ,
                                                "tablet" : 500 ,
                                                "headphone" : 150,
                                                "mouse" : 50 }
                                    
chand tabe benevisid ke in dict ra be soorate vorodi begirad va :

1. bishtarin gheymat ra bargardanad.
2. esme mahsooli ke bishtarin gheymat ra darad bargardanad.
3. hamin 2 mored ra ba baraye kamtairn gheymat ham anjam dahad.
4. jam e kole gheymate mahsoolat ra bargardanad.
5. miangin e kole mahsoolat ra bargardanad.

"""                                              

#-------------------------------------------1----------------------------------------

def maximum_price(products : dict)  :
    """
    SUMMARY : in tabe dar yek dict az mahsoolat, bishtarin gheymat ra barmigardanad.

    Parameters
    ----------
    products : dict
        DESCRIPTION : tanha vorodi in tabe yek dic az mahsoolat ast.

    Returns
    -------
    int
        DESCRIPTION : khoroji in tabe bishtarin gheymat mahsool ast.
    """
    for price in products.values():
        maximum = price
        break
    
    
    for price in products.values() :
       if price > maximum :
           maximum = price
           
    
    return maximum



products = {"laptop" : 1200,
            "phone" : 800 ,
            "tablet" : 500 ,
            "headphone" : 150,
            "mouse" : 50 }
                                    

check = maximum_price(products)     
print("Maximum price is :",check)    # Maximum price is : 1200


#---------------------------------------------2--------------------------------------

def maximum_price_name(products : dict)  :
    """
    SUMMARY : tebe baraye peyda kardane name mahsooli ke bishtarin gheymat ra darad.

    Parameters
    ----------
    products : dict
        DESCRIPTION : tanha vorodi in tabe yek dict az mahsoolat ast.

   Returns
   -------
   maximum_name : str
       DESCRIPTION : name mahsool.
   maximum : int
       DESCRIPTION : gheymat mahsool.
    """
    
    
    for product , price in products.items() :
        maximum = price
        maximum_name = product

        break
    
    
    for product , price in products.items():
        if price > maximum :
            maximum = price
            maximum_name = product
            
    return maximum_name , maximum



        
    
products = {"laptop" : 1200,
            "phone" : 800 ,
            "tablet" : 500 ,
            "headphone" : 150,
            "mouse" : 50 }
                                    

check1 , check2 = maximum_price_name(products)  
print("The",check1,"has the most price (",check2,") in products dict.")
#The laptop has the most price ( 1200 ) in products dict.   
    
    
#---------------------------------------3-1--------------------------------------------


    
    
def minimum_price(products : dict) -> int :
    """
    SUMMARY : in tabe dar yek dic kamtarin gheymat az mahsool ra peyda mikonad.

    Parameters
    ----------
    products : dict
        DESCRIPTION : tanha vorodi tabe yek dict ast.

    Returns
    -------
    int
        DESCRIPTION : khoroji in tabe kamtarin gheymat mahsool ast.
    """
    
    
    for price in products.values() :
        minimum = price
        break
    
    
    for price in products.values() :
        if price < minimum :
            minimum = price
            
    return minimum
    
    
    
 
products = {"laptop" : 1200,
            "phone" : 800 ,
            "tablet" : 500 ,
            "headphone" : 150,
            "mouse" : 50 }
                                    

check = minimum_price(products)     
print("Minimum price is :",check)   #Minimum price is : 50


#---------------------------------------3-2---------------------------------------------


def minimum_price_name(products : dict) :
    """
    SUMMARY : in tabe baraye peyda kardane name va gheymat kamtarin mahsool ast.

    Parameters
    ----------
    products : dict
        DESCRIPTION : yek dict az mahsoolat tanha vorodi in tabe ast.

    Returns
    -------
    minimum_name : str
        DESCRIPTION : name mahsool.
    minimum : int
        DESCRIPTION : gheyamt mahsool.
    """
    
    
    for product , price in products.items() :
        minimum = price
        minimum_name = product
        break
    
    for product , price in products.items() :
        if price < minimum :
            minimum = price
            minimum_name = product
            
    return minimum_name , minimum
            
            
            
    
products = {"laptop" : 1200,
            "phone" : 800 ,
            "tablet" : 500 ,
            "headphone" : 150,
            "mouse" : 50 }
                                    

check1 , check2 = minimum_price_name(products)  
print("The",check1,"has the least price (",check2,") in products dict.")            
#The mouse has the least price ( 50 ) in products dict.


#--------------------------------------4----------------------------------------------            
            
            
def total_price(products : dict) -> int:
    """
    SUMMARY : tabe ee baraye peyda kardane majmoe price haye mojod dar dict.

    Parameters
    ----------
    products : dict
        DESCRIPTION : tanha vorodi tabe ke az type dict mibashad.

    Returns
    -------
    int
        DESCRIPTION : majmoe price ha bargardande mishavad.
    """
    
    
    total = 0
    for price in products.values() :
        total += price
        
    return total



    
products = {"laptop" : 1200,
            "phone" : 800 ,
            "tablet" : 500 ,
            "headphone" : 150,
            "mouse" : 50 }
                                    

check = total_price(products)
print("Total price of dict is :", check)   #Total price of dict is : 2700
        
            
            
#-------------------------------------------5-----------------------------------------


def average_of_price(products : dict) -> float :
    
    average = total_price(products) / len(products)
    return round(average , 2)
    #ba estefade az round moshakhas mikonim chand ragham ashar dashte bashad.
    #round(number,2)---> yani number 2 ragham ashar dashte bashad.




products = {"laptop" : 1200,
            "phone" : 800 ,
            "tablet" : 500 ,
            "headphone" : 150,
            "mouse" : 50 }

check = average_of_price(products)
print("The average of price in dict is :", check)
 #The average of price in dict is : 540.0
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
           
    