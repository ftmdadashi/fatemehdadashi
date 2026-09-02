"""

7 - yek liste ghaza darim va menuye resturan hast , in list esmesh

 hast foods , aval be karbar hamash namayesh dade beeshe va done done 
 
 karbar hey entekhab kone, har zamani ke karbar nevesht ('order') dige 
 
 azash esme ghaza porside nashe, balke kole list ba estefade az for, besoorate

 factor behesh namayesh dade beshe


"""

foods = ["pitzza","pasta","burger","chicken","fries","soup","steak"]
foods_order = []

for i in foods :
    print(i)
    
while True :   
    foods_name = input("please enter your food's name :")
    
    if foods_name == "order" :
        print("-----------------------------")
        print("your order is :")

        for i in foods_order :
            print(i)
        break
    
    foods_order.append(foods_name)



"""

khoroji :
    
pitzza
pasta
burger
chicken
fries
soup
steak
please enter your food's name :pasta
please enter your food's name :fries
please enter your food's name :burger
please enter your food's name :chicken
please enter your food's name :order
-----------------------------
your order is :
pasta
fries
burger
chicken

"""
    

