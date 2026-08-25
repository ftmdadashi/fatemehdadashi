"""

Q4----Spped check

az karbar yek sorate mashin begirid

agar bish az 120 bashe benevsiid khatarnak , agar beyne 80 ta 120 bashe 
beneisid sorate ziad, agar beyne 80 ta 0 bashe benevsidi sorate noraml
agar zire 0 bashe benevsidi mashin dar halate istade hast.


"""

speed = float(input("please enter your speed :"))

if speed >= 120 :
    print("khatarnak")
    
elif speed >= 80 :
    print("sorat ziad")
    
elif speed > 0 :
    print("sorat normal")
    
else :
    print("mashin dar halate istade hast")
    
    
    
    
"""

khoroji :
    
    
please enter your speed :120
khatarnak


please enter your speed :0
mashin dar halate istade hast

    
"""