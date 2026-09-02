"""

5 - Login system --> az user , username va password begire,

 username = admin va password = 1234 hast , ta zamani ke user dorost

 username o password ro vared nakrde hey bege 'username ya password

 ghaalt mibashad' agar doros vared krd benevise : ba moafaghiat vared shodid


"""



while True :
    
    username = input("please enter your username :")
    password = input("please enter your password :")
    
    if username == "admin" and  password == "1234" :
      print("ba moafaghiat vared shodid.")
      break
            
  
    else :
        print("password  ya username ghalat ast.")
    
    
    
"""

khoroji :
    
please enter your username :1234
please enter your password :1234
password  ya username ghalat ast.
please enter your username :admin
please enter your password :1234
ba moafaghiat vared shodid.

"""
    
    
    
    
    
