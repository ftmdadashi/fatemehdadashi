"""

yek file besazid bename set_fucntions.py va set besazid va rooye
oon tavabeye set ro rosh anjam bedahid (set functions) va ba
hashtag tozih benevisid baraye har hashtag

"""

set_1 = {"abi", "sefid", "narenji"}

set_1.add("ghermez")

print(set_1)

"""

ezafe kardan moalefe jadid be set.

khoroji :
    
{'abi', 'sefid', 'ghermez', 'narenji'}

"""

set_1 = {"abi", "sefid", "narenji"}

set_1.clear()

print(set_1)

"""

khali kardan set va bargardandane set be sorate khali.

khoroji :
    
set()

"""

set_1 = {"abi", "sefid", "narenji"}

set_1.copy()

print(set_1)


"""
az set yek copy migirad va aan ra barmigardanad.

khoroji :
    
{'abi', 'sefid', 'narenji'}

"""


set_2 = {"aa", "11", "dd","ll"}
set_3 = {"dd", "aa", "gg"}

set_4 = set_2.difference(set_3) 

print(set_4)


"""

mesle mafhome riyazi (-) az majmoe aval, majmoe dovom ra hazf mikonad va 

anche dar avali mimanad, be sorate set barmigadanad.

khoroji :
    
{'11', 'll'}

"""


set_2 = {"aa", "11", "dd","ll"}
set_3 = {"dd", "aa", "gg"}

set_2.difference_update(set_3)

print(set_2)


"""

 (-=) az majmoe aval anchizi ke bein har do list moshtarak ast hazf mikonad va 

list aval ra barmigardanad.

khoroji :
    
{'11', 'll'}

"""

set_1 = {"abi", "sefid", "narenji"}

set_1.discard("abi")

print(set_1)


"""

yek moalefe moshakhas ra hazf mikonad.

khoroji:
    
{'sefid', 'narenji'}

"""


set_2 = {"aa", "11", "dd","ll"}
set_3 = {"dd", "aa", "gg"}

set_5 = set_2.intersection(set_3)

print(set_5)


"""
moshtarak dar do majmoe.(&)

khoroji:
    
{'dd', 'aa'}

"""


set_2 = {"aa", "11", "dd","ll"}

set_3 = {"dd", "aa", "gg"}

set_2.intersection_update(set_3)

print(set_2)

"""

dar in tabe alave bar intersection ya eshterak, update niz anjam mishavd va

moalefe morede nazar az majmoe aval pak mishavad.(&=)

khoroji :
    
{'dd', 'aa'}

"""



set_2 = {"aa", "11", "dd","ll"}

set_3 = {"dd", "aa", "gg"}

set_2.isdisjoint(set_3)


"""

True ra bar migardanad agar hich eshteraki bein 2 majmoe nabashd, dar gheir in 

sorat, False ra bar migardanad.

khoroji :
    
Out[15]: False

"""

set_2 = {"aa", "11", "dd","ll"}

set_3 = {"dd", "aa", "gg"}

set_2.issubset(set_3)


"""

set_2 ziir majmoe set_3 , agar dorost bashad, True va dar gheir

in sorat False.(<=)

khoroji :

Out[16]: False

"""    


set_2 = {"aa", "11", "dd","ll"}

set_3 = {"dd", "aa", "gg"}

set_2.issuperset(set_3)



"""

set_3 ziir majmoe set_2 , agar dorost bashad, True va dar

gheir in sorat False.(>=)

khoroji :

Out[17]: False

"""    


set_1 = {"abi", "sefid", "narenji"}

set_1.pop()

print(set_1)


"""

be sorate random yek moalefe ra hazf mikonad .

khoroji :
    
{'sefid', 'narenji'}

"""


set_1 = {"abi", "sefid", "narenji"}

set_1.remove("sefid")

print(set_1)


"""

yek moalefe moshakhas hazf mishavad.

khoroji :

{'abi', 'narenji'}

"""    

set_2 = {"aa", "11", "dd","ll"}

set_3 = {"dd", "aa", "gg"}

set_2.symmetric_difference(set_3)

"""

darin ravesh tamami azae moshtarak hazf mishavad, dar nahayat majmoe shamel

azae gheir moshtarak az do majmoe bar migardad.(^)

khoroji :
    
Out[20]: {'11', 'gg', 'll'}

"""



set_2 = {"aa", "11", "dd","ll"}

set_3 = {"dd", "aa", "gg"}

set_2.symmetric_difference_update(set_3)

print(set_2)

"""

darin ravesh tamami azae moshtarak hazf mishavad, dar nahayat majmoe shamel

azae gheir moshtarak az do majmoe bar migardad va majmoe aval

ra update mikonad.(^=)

khoroji :
    
{'11', 'll', 'gg'}


"""

set_2 = {"aa", "11", "dd","ll"}

set_3 = {"dd", "aa", "gg"}

set_2.union(set_3)

"""

ejtemae 2 majmoe. (|)

khoroji :
    
Out[24]: {'11', 'aa', 'dd', 'gg', 'll'}

"""

set_2 = {"aa", "11", "dd","ll"}

set_3 = {"dd", "aa", "gg"}

set_2.update(set_3)

print(set_2)

"""

alave bar ejtemae 2 majmoe, majmoe aval ra niz update mikonad. (|=)

khoroji :
    
{'dd', '11', 'll', 'aa', 'gg'}


"""


















