"""

q3.3. yek machine hesab besazid , 
yek adade (number1) yek adade number2
yechizi begire operation (jam , tafrigh,taghsim,zarb)
anjam bede print kone
 

"""

number1 = float(input("please enter your first number:"))
operation = input("please enter your operation just between (+ - / *) :")
number2 = float(input("please enter your second number:"))

if operation == "+" :
    print("jam :", number1 + number2)
    
elif operation == "-" :
    print("tafrigh :", number1 - number2)
    
elif operation == "/" :
    print("taghsim :" , number1 / number2)
    
elif operation == "*" :
    print("zarb:", number1 * number2 )
    
else :
    print("ERROR")



"""

khoroji chenin ast :
    

%runfile F:/python/3_class/session03/calculator.py --wdir
please enter your first number:32
please enter your operation just between (+ - / *) :+
please enter your second number:32
jam : 64.0

%runfile F:/python/3_class/session03/calculator.py --wdir
please enter your first number:24
please enter your operation just between (+ - / *) :-
please enter your second number:54
tafrigh : -30.0

%runfile F:/python/3_class/session03/calculator.py --wdir
please enter your first number:54
please enter your operation just between (+ - / *) :/
please enter your second number:2
taghsim : 27.0

%runfile F:/python/3_class/session03/calculator.py --wdir
please enter your first number:32
please enter your operation just between (+ - / *) :*
please enter your second number:3
zarb: 96.0


"""