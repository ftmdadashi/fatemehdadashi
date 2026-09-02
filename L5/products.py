"""

3 - az karbar hey esme mahsool begire va hey berize tooye yek 

listi bename products va inkaro onghadr edame bede ke moshtari

 benevise 'exit' va badesh kole list ro neshon bede


"""

products = input("please enter your product's name :")
products_list = []


while products != "exit" :
    products_list.append(products)
    products = input("please enter your product's name :")
    
    
print("product list =",products_list)



"""

khoroji :
    

please enter your product's name :laptop
please enter your product's name :glasses
please enter your product's name :chair
please enter your product's name :mobile
please enter your product's name :knife
please enter your product's name :t-shirt
please enter your product's name :exit
product list = ['laptop', 'glasses', 'chair', 'mobile', 'knife', 't-shirt']


"""
    
    

    