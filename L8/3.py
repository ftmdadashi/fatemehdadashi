def create_profile(name : str ,age : int , **kwargs) :
    print("- your name is : ",name)
    print("- your age is :",age)
    print("- your optional datas are :",kwargs)
    if "email" not in kwargs.keys():
        print("email not provided")
        
    if "city" in kwargs.keys() :
        print("- your city is :", kwargs["city"] )
        
    return {"name":name,"age":age,**kwargs}


check = create_profile("fatemeh", 35, city = "tehran", email = "f.dadashi")
print("your compelete data are :",check)


"""

- your name is :  fatemeh
- your age is : 35
- your optional datas are : {'city': 'tehran', 'email': 'f.dadashi'}
- your city is : tehran
your compelete data are : {'name': 'fatemeh', 'age': 35, 'city': 'tehran', 'email': 'f.dadashi'}


"""