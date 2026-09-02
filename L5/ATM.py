"""

4 - ATM --> yek system ATM sakhte beshe, be karbar bege 'Menu : mojoodi,

 variz, bardasht , khoroj , amaaliate digar' ,

 ta zamani ke karbar mojodi  , variz , bardasht ro entekhab kone baraye

 harkodom kheyli sade benevise 'amaliate variz entekhab shod , ya  
 
 amaliate felan entekhab shod' bad beporse 'amaliate digar, khoroj' , agar 
 
 amaliate diagr ro entekhab kard mojadad menu ro neshon bede 'mojoodi , 
 
 variz,bardasht' , ama agar rooye khoroj zad bege mamnon khoroj ba moafaghiat

 anajm shod
 
 """
 
 
print("........menu........")
print("mojoodi")
print("variz")
print("bardasht")
print("khoroj")
option = (input("please enter your selected option :"))


while option != "khoroj" :
    

    if option == "variz" :
        print("variz entekhab shod.")
        option = input("amaliate digar, khoroj:")
        
        if option != "khoroj":
        
            print("........menu........")
            print("mojoodi")
            print("variz")
            print("bardasht")
            print("khoroj")
            option = (input("please enter your selected option :"))

        else :
            print("khoroj ba moafaghiayat anjam shod.")
            break
        
        
        
    elif option == "bardasht" :
        print("bardasht entekhab shod.")
        option = input("amaliate digar, khoroj:")
        
        if option != "khoroj":
        
            print("........menu........")
            print("mojoodi")
            print("variz")
            print("bardasht")
            print("khoroj")
            option = (input("please enter your selected option :"))
            
        else :
             print("khoroj ba moafaghiayat anjam shod.")
             break


        
    elif option == "mojoodi" :
        print("mojoodi entekhab shod.")
        option = input("amaliate digar, khoroj:")
        
        if option != "khoroj":
        
            print("........menu........")
            print("mojoodi")
            print("variz")
            print("bardasht")
            print("khoroj")
            option = (input("please enter your selected option :"))

        else :
             print("khoroj ba moafaghiayat anjam shod.")
             break
        
        
        
        
        
        
"""

khoroji :
    
    
........menu........
mojoodi
variz
bardasht
khoroj
please enter your selected option :mojoodi
mojoodi entekhab shod.
amaliate digar, khoroj:amaliate digar
........menu........
mojoodi
variz
bardasht
khoroj
please enter your selected option :variz
variz entekhab shod.
amaliate digar, khoroj:amaliate digar
........menu........
mojoodi
variz
bardasht
khoroj
please enter your selected option :bardasht
bardasht entekhab shod.
amaliate digar, khoroj:khoroj
khoroj ba moafaghiayat anjam shod.


"""
        
        
        
        
        
        
        
        
        
