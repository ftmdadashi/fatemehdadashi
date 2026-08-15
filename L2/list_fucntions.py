"""

yek file besazid bename list_fucntions.py va listi besazid va rooye
oon tavabeye list ro rosh anjam bedahid (list functions) va ba
hashtag tozih benevisid baraye har hashtag


"""

l_1 = ["fatemeh", "dadashi"]

l_2 = ["sadat"]

l_1.append(l_2)

print(l_1)


"""

dar in tabe mitavn list ha ra ba ham edgham kard. list dovom dar entehaye

list aval ezafe mishava. havaset bashe list dovom be sorate list ezafe mishavad.


khoroji chenin ast :
    
['fatemeh', 'dadashi', ['sadat']]    
       
    
"""    


l_3 = ["abi", "zard ","narenji", "ghermez"]

l_3.clear()

print(l_3)


"""

moalefehaye list ra pak mikonad va tanha yek list khali barmigardanad.

khoroji be sorate zir ast :
    
[]

"""


l_3 = ["abi", "zard ","narenji", "ghermez"]

l_4 = l_3.copy()

print("l_4 :",l_4)


"""

az list copy gerefte va dar motrghayer jaid mirizad.

khoroji be sorate zir ast :
    
l_4 : ['abi', 'zard ', 'narenji', 'ghermez']    
    
"""


l_5 = [ 1, 2, 9, 8, 7, 7, 7, 5]

tedad = l_5.count(7)

print("tedade 7 :",tedad)


"""

tedad tekrarhaye yek moalefeye moshakhas ra taeen mikonad.

khoroji be sorate zir ast :
    
tedade 7 : 3

"""


l_6 = ['maryam', 'farideh', 'afsaneh']

l_7 = ['mobin', 'samin']

l_6.extend(l_7)

print(l_6)


"""

gostaresh dadane yek list, havaset bashe inja bar khalafe append, list 

ezafe nmishe, balke faghat moalefeha be entehaye list aval ezafe mishavad.

khoroji be sorate zir ast :
    
['maryam', 'farideh', 'afsaneh', 'mobin', 'samin']

"""


l_7 = ['python', 'c++', 'java']

x = l_7.index("c++")

print(x)


"""

index marboot be variable made nazar dar list ra bar migardanad.

khoroji be sorate zir ast :
    
1

"""

l_8 = ['siyah', 'sefid']

l_8.insert(2, "banafsh")

print(l_8)


"""

ezafe kardane yek moalefe be index e delkhah. 

khoroji chenin ast :
    
['siyah', 'sefid', 'banafsh']

"""

l_9 = ["1370", 1370, "1371"]

l_9.pop(1)

print(l_9)


"""

in tabe moalefe marboot be index vared shode ra hazf mikonad.

khoroji be sorate zir ast :
    
['1370', '1371']

"""

l_10 = ["riyazi", "fizik", "shimi" ]

l_10.remove("riyazi")

print(l_10)


"""

dar in tabe bayad barkhalafe pop ke indx vared mikardi, khode moalefe vared 

beshe.

khoroji be sorate zir ast :
    
['fizik', 'shimi']

"""

l_11 = ["aval","dovom","sevom"]

l_11.reverse()

print(l_11)


"""

in tabe list ra bar aks mikona.

khoroji be sorate zir ast :
    
['sevom', 'dovom', 'aval']

"""

l_12 = ["MVM", "TOYOYA", "benz" , "13" , "14"]

l_12.sort()

print(l_12)


"""

in tabe bar asase horof list ra sort mikonad. tavajoh kon ke horof captal

ra dar olaviat gharar midahad, hamchenin adaad ra ke be sorate string 

vared shodeh be horof (a-z) dar olaviat gharar midahad.

khoroji chenin ast :
    
['13', '14', 'MVM', 'TOYOYA', 'benz']


"""
