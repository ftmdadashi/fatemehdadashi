"""

# 17_Menu_app.py

yek tabe besazid ke vorodie e nagire balke dakhelesh yek while shoro she 
yek menu az ghaza biare , va ta zamani ke user 'order' ro nazade hey 
azash (input) begire va vaghty tamom shod, tamame ordere moshtari ro dakhele 
yek list berize va list ro khoroji bede

"""


def Menu_app():
    """
    SUMMARY " tabee baraye menu yek resturan ke ta zamani ke order vared nashode
    az user list ghaza migire."

    Returns
    -------
    None
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
            break
    
        foods_order.append(foods_name)

    for i in foods_order :
        print(i)
        
        
        
Menu_app()

    
"""

pitzza
pasta
burger
chicken
fries
soup
steak
please enter your food's name :fries
please enter your food's name :chicken
please enter your food's name :pasta
please enter your food's name :pitzza
please enter your food's name :order
-----------------------------
your order is :
fries
chicken
pasta
pitzza

"""    
    
    
    
            
        
   

