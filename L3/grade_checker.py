"""


q3.4. nomreye daneshjo ro begri eye adadi beyne 0 ta 20

ag 18 - 20 --> A
16 0 18 --> B

14-16 --C
10-14 --> d

<10 --> f (faill)
 

"""

grade = float(input("please enter your grade between (0-20) :"))

if grade > 20 :
    print('not acceptable grade, grade can be less than 20 ')

elif grade>=18 :
    #inja yani na balaye 20 hast va balaye 18 hast
    #yani hamoon beyne 20 ta 18
    print("Your grade is A")
    
elif grade>=16 :
    #inja na balaye 20 hast , na balaye 18 . pas yani zire 18 hast
    #va shart mige bayad balaye 16 bashe
    #yani beyne 18 ta 16
    print("Your grade is B")
    
elif grade>=14 :
    #hamchnin inja yani beyne 14 ta 16 
    print("Your grade is C")
    
elif grade>=10 :
    print("Your grade is D")
    
else:
    #inja else yani , hichkodom az shart haye bala nist
    #yani na balaye 20 , na baal 18 , 16 , 14, 10 
    #pas yani vaghty ke zire 10 hast in hamon else hast
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









