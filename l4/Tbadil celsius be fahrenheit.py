"""


Q10----Tbadil celsius be fahrenheit

Ma yek dade darim az sensore yek karkhane ke dama ro be Celsius neveshte ast.

yek liste jadid besazid va in list bayaad adade farenheite ghabli ha bashad

formule tabdil : Farenheit = Celsius * 1.8 + 32


"""

celsius = [35,45,55,75,86]
farenheite = []

for temp in celsius :
    tem = temp * 1.8 + 32
    farenheite.append(tem)
    
    
print("celsius is =",celsius)
print("farenheite is =",farenheite)




"""

khoroji :
    

celsius is = [35, 45, 55, 75, 86]
farenheite is = [95.0, 113.0, 131.0, 167.0, 186.8]


"""