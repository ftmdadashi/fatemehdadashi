"""

4. yek tabe benevisid ke yek tuple az tuple ha ra be onvane vorodi code

daryaft konad.

sales = (
("Ali", "Laptop", 1200),
("Sara", "Phone", 800),
("Ali", "Phone", 800),
("Reza", "Laptop", 1200),
("Sara", "Laptop", 1200),
("Ali", "Mouse", 50)
)

1. yek tabe benevisid ke khoroji aan yek dictionary bashad, be toori ke

kelid, har fard va joloye aan jame kharidhaye aan fard gharar begirad.

2. yek tabe benevisid ke khoroji aan yek dictionary bashad, kelid ha esme

mahsoolat bashand va joloye harkodam tedad e forosh aan mahsool gharar

begirad.

3. yek tabe benevisid ke khoroji aan yek adad bashad ke majmoe daramade 

foroshgah ra neshan dahad.

"""

#----------------------------------------1----------------------------------------------

def total_price(sales : tuple) -> dict : 
    """
    SUMMARY : tabe ee baraye yaftan majmoe kharid haye har fard.

    Parameters
    ----------
    sales : tuple
        DESCRIPTION : vorodi tabe yek tuple ast.

    Returns
    -------
    dict
        DESCRIPTION : khoroji tabe yek dict ast ke key aan name afrad va 
        value aan majmoe price ha mibashad.
    """
    
    
    dict_tatal_price = {}
    for information in sales :
            if information[0] in dict_tatal_price :
                dict_tatal_price[information[0]] += information[2]
                
            else :
                dict_tatal_price[information[0]] = information[2]


    return dict_tatal_price 

    



sales = (
("Ali", "Laptop", 1200),
("Sara", "Phone", 800),
("Ali", "Phone", 800),
("Reza", "Laptop", 1200),
("Sara", "Laptop", 1200),
("Ali", "Mouse", 50)
)

check = total_price(sales)
print("Majmoe kharidhaye har fard =", check)
#Majmoe kharidhaye har fard = {'Ali': 2050, 'Sara': 2000, 'Reza': 1200}



#----------------------------------------2-----------------------------------------


def numbers_of_products(sales : tuple) -> dict :
    """
    SUMMARY : tabe ee baraye peyda kardane tedade mahsoolat.

    Parameters
    ----------
    sales : tuple
        DESCRIPTION : vorodi yek tuple ast.

    Returns
    -------
    dict
        DESCRIPTION : khoroji yek dict az mahsoolat ba key az name mahsool va
        value az tedade aan ast.
    """
    
    
    products_list = {}
    for information in sales :
        if information[1] in products_list :
            products_list[information[1]] += 1
            
        else :
            products_list[information[1]] = 1
            
        
    return products_list


sales = (
("Ali", "Laptop", 1200),
("Sara", "Phone", 800),
("Ali", "Phone", 800),
("Reza", "Laptop", 1200),
("Sara", "Laptop", 1200),
("Ali", "Mouse", 50)
)

check = numbers_of_products(sales)
print("The numbers of products =", check)
#The numbers of products = {'Laptop': 3, 'Phone': 2, 'Mouse': 1}



#----------------------------------------3----------------------------------------------

def total_income(sales : tuple ) -> int :
    """
    SUMMARY : tabe ee baraye peyda kardne daramade koli foroshgah.

    Parameters
    ----------
    sales : tuple
        DESCRIPTION : vorodi tabe.

    Returns
    -------
    int
        DESCRIPTION : khoroji tabe ke yek adad ast.
    """
    
    
    total_price = 0
    for information in sales :
        total_price += information[2]
        
    return total_price



sales = (
("Ali", "Laptop", 1200),
("Sara", "Phone", 800),
("Ali", "Phone", 800),
("Reza", "Laptop", 1200),
("Sara", "Laptop", 1200),
("Ali", "Mouse", 50)
)


check = total_income(sales)
print("The total income is :", check)   #The total income is : 5250













