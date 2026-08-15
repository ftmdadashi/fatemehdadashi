"""

q3.4. nomreye daneshjo ro begri eye adadi beyne 0 ta 20

ag 18 - 20 --> A
16 0 18 --> B

14-16 --C
10-14 --> d

<10 --> f (faill)
 

"""

grade = float(input("please enter your grade between (0-20) :"))

if (grade >= 18) and (grade <= 20) :
    print("Your grade is A")
    
if  (grade >= 16) and (grade < 18) :
    print("Your grade is B")
    
if  (grade >= 14) and (grade < 16):
    print("Your grade is C")
    
if  (grade >= 10) and (grade < 14) :
    print("Your grade is D")
    
if  (grade < 10) :
    print("FAILL")
    
    
    
    
"""

ba tavajoh be taarife koli bazeha, chenin farz shodeh ast ke dar 
baze aval [18,20], baze dovom [16,18), baze sevom [14,16), baze chaharom
[10,14) va baze akhar [0,10) mibashad. chon dar gheir in sorat nmitavan 
dasteye moshakhasi baraye adade mojod dar ebteda va entehaye baze moshakhas
nemood.

""" 



"""

khoroji chenin ast:
  
%runfile F:/python/3_class/session03/grade_checker.py --wdir
please enter your grade between (0-20) :14
Your grade is C

%runfile F:/python/3_class/session03/grade_checker.py --wdir
please enter your grade between (0-20) :18
Your grade is A

%runfile F:/python/3_class/session03/grade_checker.py --wdir
please enter your grade between (0-20) :12
Your grade is D

%runfile F:/python/3_class/session03/grade_checker.py --wdir
please enter your grade between (0-20) :17
Your grade is B    
  
    
  
"""



















