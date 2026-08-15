"""

Aval yek file besazid bename str_functions.py va random name ='esme khodeton' 

ya harchizi va bad tak take tavabeye string ro (string functions). ro roosh ejra 

konid va  ba hashtag comment konid va toizh bedid ke har tabe che kari ro mikone


"""


name_1 = input("Please enter your name for capitalize:")

print(name_1.capitalize())



"""
tabe capitalized faghat dar morede string hast va tanha harf aval string ra 

captal mikonad. tavajoh kon k agar dar neveshtan esme made nazaret ba space 

shoro koni harf aval ro hamon space dar nazar migire. hamchenin harchizi joz 

string ra dar nazar nmigirad ( masalan adad)


ba farze name_1 : fatemeh

khoroji chenin ast : 
    
Please enter your name for capitalize:fatemeh
Fatemeh


   

"""

name_2 = input("Please enter your name for casefold & lower :")


print(name_2.casefold())

print(name_2.lower())


"""

in  2 tabe bar roye har string ejra shode va tamame horofe captal ro be small

tabdil mikonand. 



ba farze name_2 :FATEMEH 

khoroji chenin ast : 
    
Please enter your name for casefold & lower :FATEMEH
fatemeh
fatemeh

"""


name_3 = input("Please enter your name for center:")

print(name_3.center(20,"*"))


"""

in tabe string ra gerefte va barasas toli ke barayash tarif mikonim, 

string made nazar ra daghighan dar markaz an gharar midahad. 

center(length, character) darvaghe taeen konande tole kole stringe khoroji va 

hamchenin character, string made nazare ma baraye ghab va bad az vorodi ast 

ke be sorat deafalt space dar nazar gerefte mishavad . 



ba farze name_3  :fatemeh 

koroji chenin ast : 
    
Please enter your name for center:FATEMEH
******FATEMEH*******


"""

name_4 = input("Please enter your name for count :")

print(name_4.count("a"))


"""

in tabe ba gereftan string be onvan vorogi tedad tekrarhaye stringe made 

nazare ma ro dar vorodi taeen mikonad. string.count(value, start, end)

dar vaghe value vazhe made nazare mast, start jaygahe shoroe jost o jo

dar stringe vorodi va end jaygahe payan ast ke be sorate pish farz, aval 

va akhar string e vorodi dar nazar gerefte mishavad.


ba farze name_4 :FATEMEH

khoroji chenin ast :
    
Please enter your name for count :FATEMEH
0


"""



name_5 = input("Please enter your name for encode:")

print(name_5.encode())


"""

ba dastore encode, vorodi be utf-8 tabdil mishavad.

ba farze name_5 :fatemeh

khoroji chenin ast :
    
Please enter your name for encode:FATEMEH
b'FATEMEH'


"""



name_6 = input("Please enter your name for endswith:")

print(name_6.endswith("f"))


"""

in tabe taeen mikonad ke aya stringe vorodi ba stringe moshakhasi tamam 

mishavd ya kheir. ba check kardan in moozo tanha True va ya 

False barmigardanad. string.endswith(value, start, end) , start va end 

be sorate optional baraye taeen position shoro va payan mibashand.

ba farze name_6 :fatemeh 

khoroji chenin ast :
    
Please enter your name for endswith:FATEMEH
False

"""




name_7 = input("Please enter your name for find & index :")


print(name_7.find("h"))

print(name_7.index("h"))


"""

har do tabe bala baraye peyda kardan avalin* substring made nazare ma 

morede estefade ghara migirad va index aan ra be onvane khoroji namayesh

midahad. tanha tafavote in do tabe zamani ast ke harfe made nazar peyda nashavad

dar in sorat, tabe find meghdar -1 va tabe index, ValueError: substring not found

ra namayesh midahad.


ba farze name_7 :fatemeh 

khoroji chenin ast :
    
Please enter your name for find & index : fatemeh
7
7
    
"""


name_8 = input("Please enter your sentence for format :")

print(name_8.format("abi"))


"""

ba estefade az in tabe harchizi ra mitavan dar {} jaygozin kard, dar vaghe 

curly brackets baraye hefz va jaygozini ebarate khas morede estefade gharar

migirad . 

ba farze name_8 =aseman {} ast 

khoroji chenin ast :
    
Please enter your sentence for format :aseman {} ast
aseman abi ast


"""


name_9 = input("Please enter your sentence for format_map :")

diic = {"name":"fatemeh" , "last name":"dadashi"}

print(name_9.format_map(diic))



"""

dar in tabe kalmate moshakhas ba estefade az dictionary dar  {}

jay gozari mishavand .



ba farze name_9 : my name is {name} {last name}

khoroji chenin ast :
    
Please enter your sentence for format_map : my name is {name} {last name} 
 my name is fatemeh dadashi 


"""


name_10 = input("Please enter your sentence for isalnum :")

print(name_10.isalnum())


"""

az in tabe baraye baresiye string estefade mishavad. agar string shamele 

horof ( a-z ) & adad ( 0-9 ) bashad meghdare True va dar gheire in sorat 

mrghdar False ra barmigardanad.


khoroji ba vorodihaye moteghayer be sorate zir ast :
    

Please enter your sentence for isalnum :%$$#fdgb
False


Please enter your sentence for isalnum :fgfddjj7678
True


"""



name_11 = input("Please enter your sentence for isalpha :")


print(name_11.isalpha())


"""

az in tabe baraye barresi letter bodane tamamie horof dar string estefade 

mishavad .

khoroji be sorate zr ast :
  
Please enter your sentence for isalpha :f1aftem4eh
False     
    

"""


name_12 = input("Please enter your sentence for isascii :")


print(name_12.isascii())


"""

az in tabe baraye barresi ascii  bodane tamamie horof dar string estefade 

mishavad .

khoroji be sorate zr ast :


Please enter your sentence for isascii :fatemeh123456
True

"""



name_13 = input("Please enter your sentence for isdecimal :")


print(name_13.isdecimal())




"""

az in tabe baraye barresi decimal(0-9) bodane tamamie horof dar string estefade 

mishavad .

khoroji be sorate zr ast :


Please enter your sentence for isdecimal :123654
True


Please enter your sentence for isdecimal :125fgd
False



"""


name_14 = input("Please enter your sentence for isdigit :")

print(name_14.isdigit())


"""

az in tabe baraye barresi adade dahdahi (0-9) bodane tamamie horof va 

hamchenin bazi charactor adadi mesle javan dar string estefade 

mishavad .

khoroji be sorate zr ast :
    

Please enter your sentence for isdigit :fa125
False

Please enter your sentence for isdigit :123434
True


"""


name_15= input("Please enter your sentence for isidentifier :")

print(name_15.isidentifier())


"""

baraye barresi ghabele tarif bodane string morede estefade gharar migirad.

agar shamele (a-z) & (0-9) bashad ghabele ghabol ast vali estefade az adad 

baraye shoro va ya space dar string gheire ghabele ghabol ast.


khoroji be sorate zr ast :
    
Please enter your sentence for isidentifier :__fate123
True


Please enter your sentence for isidentifier :fa    te  001
False    
    
    
Please enter your sentence for isidentifier :1fat123
False    
    
    
"""   


name_16= input("Please enter your sentence for isnumeric :")

print(name_16.isnumeric())


"""

az in tabe baraye barresi reshte be onvane (0-9) va hamchenin tavan 

estefade mishavad.

khoroji be sorate zir ast :
    
Please enter your sentence for isnumeric :12354
True    
    
    
Please enter your sentence for isnumeric :hgj123
False    
    
    
"""


name_17= input("Please enter your sentence for isprintable :")

print(name_17.isprintable())


"""

baraye barresi ghabele print kardan e tamame vorodi ast.

khoroji be sorate zir ast :
  
    
Please enter your sentence for isprintable :fa   #t
True  
    
     
"""


name_18= input("Please enter your sentence for isspace :")

print(name_18.isspace())


"""

az in tabe baraye barresi yek fazaye khali estefade mishavd dar gheir in 

sorat False barmigardanad.

khoroji be sorate zir ast :
    

Please enter your sentence for isspace :     
True


Please enter your sentence for isspace :""
False


"""

name_19= input("Please enter your sentence for istitle :")

print(name_19.istitle())


"""

dar yek string harf avale tamami title ha ro barresi mikone agar
captal boodan (True) dar gheir in soorat (False ).

khoroji be sorate zir ast :

Please enter your sentence for istitle :Aseman Ziba
True


Please enter your sentence for istitle : aseman zib ast.
False

"""

name_20= input("Please enter your sentence for isupper :")

print(name_20.isupper())


"""

agar tamami horof captal bashand (True) dar gheir in sorat (False)

khoroji be sorate zir ast :
    
Please enter your sentence for isupper :FAT123
True    
    
"""



name_21= input("Please enter your sentence for ljust & rjust :")


print(name_21.ljust(20,"*"))


print(name_21.rjust(20,"*"))


"""

dar in tabe vorodi gerefte mishavad va ba tavajoh be inke dar rjust va ya

ljust gharar gerefte ast be rast va ya chap align mishavad. dar mesale bala

20 tole koli khoroji ast ke bakhshi az aan ra string va baghi aan ra * (optional)

por karde ast.

khoroji be sorate zir ast : 
    
Please enter your sentence for ljust & rjust : fatemeh

 fatemeh************
************ fatemeh    

"""


name_22 = input("Please enter your sentence for strip & lstrip & rstrip :")

print(name_22.strip())

print(name_22.lstrip())

print(name_22.rstrip())



"""

az in tavabe baraye hazf kardane fazaye khali (pish farz) dar atrafe string

estefade mishavd, strip, tamame space haye rast va chap, lstrip faghat space haye 

left va rstrip space haye rast ra hazf mikonad.

mitavan strip("string") ra niz estefade kard, dar in sorat string made nazar 

ra hazf mikonad.


khoroji be sorate zir ast :

    
Please enter your sentence for strip & lstrip & rstrip :          fatemeh

fatemeh
fatemeh
          fatemeh

"""


name_23 = input("Please enter your sentence for translate & maketrans :")

print(name_23.translate(str.maketrans("e","z", "t")))



"""

dar in tavabe dar ebteda ba estefade az str.maketrans jadvali dorost mishavad

ke moalefe aval ra ba dovomi dar tamami string jaygozin mikonad va moalefe 

sevom dar tamami string hazf khahad shod. be oonvan mesal dar bala be jaye "e" 

---> "z"  gharar gerefteast va "t" kamelan hazf shode ast.

az tabe translate niz baraye n jaygozariha va sakhte string jadid 

estefade mishavad.


khorojo be sorate zir ast :
    
Please enter your sentence for translate & maketrans :fateeeemeeehhttt

fazzzzmzzzhh    


"""


name_24 = input("Please enter your sentence for partition & rpartition :")

print(name_24.partition("dadashi"))

print(name_24.rpartition("dadashi"))


"""

dar in tavabe partition bandi jomle ba estefade az string moshakhas shode

anjam mishavad. khoroji aan yek tuple mibashad ke daraye 3 bakhsh ast.

partition ----> ("samte chape string", "string","samte raste string")

agar dar in tabe string made nazar peyda nashavad dar in sorat  

--------> ("vorodi vared shodeh", " "," ")


rpartition -----> migarde toye vorodi akharin string made nazaret ro peyda 

mikoe, hala barasas oon -------> 

("samte chape string made nazar","strin made nazar", "samte rast string")

agar string made nazar dar vorodi nabahad ----> ("","","vorodi vared shodeh")


khoroji be sorae zir ast :
    
Please enter your sentence for partition & rpartition :my name is fatemh dadashi
('my name is fatemh ', 'dadashi', '')
('my name is fatemh ', 'dadashi', '')    


Please enter your sentence for partition & rpartition : dadashi, fatemeh sadat dadashi
(' ', 'dadashi', ', fatemeh sadat dadashi')
(' dadashi, fatemeh sadat ', 'dadashi', '')

"""


name_25 = input("Please enter your sentence for rfind & rindex :")

print(name_25.rfind("a"))

print(name_25.rindex("a"))


"""

baraye peyda kardan char moshakhasi estefade mishavad.

khoroji be sorate zir ast :
    
Please enter your sentence for rfind & rindex : faaatemeh
4
4

(chon fatemeh ro ba space shoro kardi)



Please enter your sentence for rfind & rindex :fatemeh
1
1


"""


name_25 = input("Please enter your sentence for startwith :")

print(name_25.startswith("hello"))


"""

baraye check kardan shoro vorodi ba string made nazar ast, True ya False 

barmigardanad.

khoroji be sorate zir ast :
    
Please enter your sentence for startwith :hello, my name is fatemeh
True    

"""


name_26 = input("Please enter your sentence for swapcass :")

print(name_26.swapcase())


"""

horof captal ra be small va bar aks tabdil mikonad.

khoroji be sorate zir ast :
    
    
Please enter your sentence for swapcass :Hello, MYnamE iS fatEmeh
hELLO, myNAMe Is FATeMEH

""" 


name_27= input("Please enter your sentence for zfill :")

print(name_27.zfill(20))


"""

be andaze toole taeen shode 0 be string ezafe mikonad. (havaset bashe 
                                                        
majmoe string ba sefrha mishavd toole made nazar)

khoroji be sorate zir ast :
    
Please enter your sentence for zfill :fatemeh
0000000000000fatemeh

"""


name_28= input("Please enter your sentence for splitline :")


print(name_28.splitlines())



"""

bar asase line break, vorodi ra be yek list tabdil mikonad.

khoroji be sorate zir ast :
    
Please enter your sentence for splitline :fatemeh dadashi
['fatemeh dadashi']


"""











