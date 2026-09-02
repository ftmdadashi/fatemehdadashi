"""

1 - Yek listi az nomreye daneshjooha darim , varede in list beshe va 
daneshjoohaye failed va pass ro dar biare

scores = [20,17,9 , 13, 7 , 20 , 18 , 3 , 1 , 14]


"""

scores = [20,17,9 , 13, 7 , 20 , 18 , 3 , 1 , 14]
student = 0


for num in scores :
    student += 1
    if num >= 10 :
        print("student",student,"with score",num,"is passed.")
        
        
    else :
        print("student",student,"with score",num,"is failed.")

        
        
        
"""

dar in barname baraye har daneshjoo barasase jaygahash dar list az 1 ta 10

position gharar dadeim.

khoroji :
    
    
student  1 with score  20 is passed.
student  2 with score  17 is passed.
student  3 with score  9 is failed.
student  4 with score  13 is passed.
student  5 with score  7 is failed.
student  6 with score  20 is passed.
student  7 with score  18 is passed.
student  8 with score  3 is failed.
student  9 with score  1 is failed.
student  10 with score  14 is passed.


"""