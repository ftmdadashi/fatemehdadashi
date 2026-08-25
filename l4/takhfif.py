"""


Q2----- Takhfif
az user gheymate kala ro begirid , age gheymate kala bishtar az 1 milion toman bashad
20% takhfif, agar gheymate kala beyne 500,000 ta 1 million toman bashe , 15 darsad takhfif 
agar gheymate kala zire 500 hezar toman bashad, 10% takhfif emal konid va dar nahayat
gheymate bad az takhfif ro b user neshan dahid


"""

price = int(input("please enter price :"))

if price >= 1000000 :
    price = price - (price * 0.2)
    
elif price >= 500000 :
    price = price - (price * 0.15)
    
else :
    price = price - (price * 0.1)
    
    

print("Dear user, your final price is :", price)




"""

khoroji :
    
please enter price :12000000
Dear user, your final price is : 9600000.0



please enter price :500
Dear user, your final price is : 450.0

"""