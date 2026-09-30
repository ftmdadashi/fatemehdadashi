def available_products(products : dict) :
    for product , stock in products.items() :
        if stock > 0 :
            yield product
            
            
            
products = {"laptop":3,
            "phone":0,
            "tablet":5,
            "mouse":0,
            "keyboard":2}


check = available_products(products)
print(next(check))     #laptop
print(next(check))     #tablet
print(next(check))     #keyboard
print(next(check))     #StopIteration