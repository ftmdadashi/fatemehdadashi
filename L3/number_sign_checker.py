"""

q3.1 Yek adad begire az karbar, bebine positive, negative, zero.


"""




number = float(input("Hello, please enter your number for sign checking :"))

if number > 0 :
    print("number",number,"is positive")
    
elif number == 0 :
    print("number",number, "is zero")
    
else :
    print("number",number, "is negative")


"""

ba tavajoh be inke addad positive bozogtar az 0 mibashand va shamele 
addade ashari niz mibashand az float estafade shode ast. 

"""


"""

khoroji chenin ast:
 
%runfile F:/python/3_class/session03/number_sign_checker.py --wdir
Hello, please enter your number for sign checking :-23
number -23.0 is negative

%runfile F:/python/3_class/session03/number_sign_checker.py --wdir
Hello, please enter your number for sign checking :24
number 24.0 is positive

%runfile F:/python/3_class/session03/number_sign_checker.py --wdir
Hello, please enter your number for sign checking :0
number 0.0 is zero    
    
    
    
"""