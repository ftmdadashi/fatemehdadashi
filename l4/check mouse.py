"""

Q3---- check mouse
ma yek list darim az mahsoolat , va injori hast : 
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

yek vorodi az karbar begirid va az karbar bekahhdi esme yek mahsol ro bege
agar oon mahsol dakhele in list bashe begid mahsool dar dastress hast , 
agar nabood benevisid dar dastress nist.

"""


products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
user_product = input("please enter your product 's name :").title()

if user_product in products :
    print(user_product,"dar dastres ast")
    
else :
    print(user_product,"dar dastres nist")
    
    
    
"""

khoroji :
    
please enter your product 's name :KEYYBORD
Keyybord dar dastres nist


please enter your product 's name :lapTOP
Laptop dar dastres ast


please enter your product 's name :KEYYBORD
Keyybord dar dastres nist


"""