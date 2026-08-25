"""

Q9----Afzayeshe gheymat
yek listi darim az gheymate mahsol haye yek foroshgah , yek liste jadid besazid
ke tamame gheymate mahsoolat ro 10% afzayesh dahad.

"""


first_price = [1200000,1500000,3500000,2000000]
second_price = []

for price in first_price :
    price = price + price * 0.1
    second_price.append(price)
    

print("first_price =",first_price)
print("second_price =",second_price)




"""

khoroji :
    
 
first_price = [1200000, 1500000, 3500000, 2000000]
second_price = [1320000.0, 1650000.0, 3850000.0, 2200000.0]    
    
    
"""