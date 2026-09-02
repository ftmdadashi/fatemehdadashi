"""

6 - hamin login system ro hbenevisind be sharti ke agar bish az 3 bar

 ehstebah vared kard , begid account ghofl shode va dige nazarid username 
 
 ya password bezane va ende program


"""

i = 0

while i < 3 :
    
    username = input("please enter your username :")
    password = input("please enter your password :")
    i += 1
    
    if username == "admin" and  password == "1234" :
      print("ba moafaghiat vared shodid.")
      break
            
  
    else :
        print("password  ya username ghalat ast.")
    
print("__________________________________________")    
print("you are blocked.")