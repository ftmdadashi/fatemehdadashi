"""

# 18_user_management.py

yek systeme sade modiriat karbar msiazim

ma yek listi az user ha(dictionary) darim ke etelaateshon hastand , in list ro
 mitonid ba estefade az gpt hata boizorgtaresh ham konid

```python
users = [
    {
        "username": "ali",
        "age": 25,
        "city": "Tehran",
        "active": True
    },
    {
        "username": "sara",
        "age": 17,
        "city": "Tabriz",
        "active": True
    }
]
```


a) yek tabe besazid bename 

```python
add_user(users, username, age, city)
```

in biad hamon user ro dictionary kone va be oon products ezafe kone va active ham pish farz True 
hast , va badesh liste user ha update shode ro bargardoone



b) Hala yek tabe besazid bename

```python
find_user(users, username)
```

ke biad tooye oon list begarde oon user ro peyda kone agar vojod nadasht None pas bede, agarvojod
 dasht dictionary marboot be user ro pas bede

c) yek tabe beszid ke check kone oon user ejaze dastresi dare ya na

```python
check_access(users, username)
```

baayd vase oon username check kone agar age>=18 va active bashe true pas bede, agar na False pas bede


d) yek tabe benvisid

```python
get_adult_users(users)
```

va faghat karbar haye balaye 18 sale ro dar yek list gharar bede va oon list ro pas bede.




tamame in 4 tabe ro dakheel file bename 18_user_management.py benevisid.

"""


#----------------------------------------a--------------------------------------



def add_user(users :list , username : str , age : int, city : str ) -> list :
    """
    SUMMARY : tabe ke mitavanad yek user jadid ra be sorate dict zakhireh
    karde va be list userha ezafeh konad.

    Parameters
    ----------
    users : str
        DESCRIPTION : vorodi aval.
    username : str
        DESCRIPTION : vorodi dovom.
    age : int
        DESCRIPTION. : vorodi sevom.
    city : str
        DESCRIPTION : vorodi chaharom.

    Returns
    -------
    list
        DESCRIPTION :  khoroji tabe yek list update shode ast.
    """
    
    user = {"username": username , "age": age , "city": city ,"active" :True}
    users.append(user)
    return users





 
users = [{ "username": "ali","age": 25,"city": "Tehran","active": True },
         {"username": "sara","age": 17,"city": "Tabriz","active": True},
         {"username": "fatemeh","age": 35,"city": "Esfehan","active": True},
         {"username": "maryam","age": 19,"city": "Hamedan","active": False},
         {"username": "roya","age": 30,"city": "ghazvin","active": True},
         {"username": "amin","age": 37,"city": "Ardebil","active": False}]

check = add_user(users, "elenna", 25, "dezfool")
print(check)
    

"""
[{'username': 'ali', 'age': 25, 'city': 'Tehran', 'active': True},
 {'username': 'sara', 'age': 17, 'city': 'Tabriz', 'active': True},
 {'username': 'fatemeh', 'age': 35, 'city': 'Esfehan', 'active': True},
 {'username': 'maryam', 'age': 19, 'city': 'Hamedan', 'active': False},
 {'username': 'roya', 'age': 30, 'city': 'ghazvin', 'active': True},
 {'username': 'amin', 'age': 37, 'city': 'Ardebil', 'active': False},
 {'username': 'elenna', 'age': 25, 'city': 'dezfool', 'active': True}]

"""


 #----------------------------------------b----------------------------------------


def find_user(users : list , username : str) :
    """
    SUMMARY : tabee baraye peyda kardane dict marboot be karbar ba estefade az 
    username.

    Parameters
    ----------
    users : list
        DESCRIPTION : vorodi aval.
    username : str
        DESCRIPTION : vorodi dovom

    Returns
    -------
    user : TYPE
        DESCRIPTION : agar username mojod bod, dict aan va dar gheir in soorat
        None bargardande mishavad.
    """
    
 
    for user in users :
        if user["username"] == username :
            return user 
            
    return None
        
        
        

users = [{ "username": "ali","age": 25,"city": "Tehran","active": True },
     {"username": "sara","age": 17,"city": "Tabriz","active": True},
     {"username": "fatemeh","age": 35,"city": "Esfehan","active": True},
     {"username": "maryam","age": 19,"city": "Hamedan","active": False},
     {"username": "roya","age": 30,"city": "ghazvin","active": True},
     {"username": "amin","age": 37,"city": "Ardebil","active": False}]
check = find_user(users, "maryam")
print(check)
    
 
"""
{'username': 'maryam', 'age': 19, 'city': 'Hamedan', 'active': False}

"""


#----------------------------------c----------------------------------------------


def check_access(users : list, username : str) -> bool :
    """
    SUMMARY : tabee baraye mahdodiate dastresi user az tarighe filterhaye moshakhas:
        age va active

    Parameters
    ----------
    users : list
        DESCRIPTION : vorodi aval
    username : str
        DESCRIPTION : vorodi dovom

    Returns
    -------
    bool
        DESCRIPTION : khoroji True va ya False ast.
    """
    
    for user in users :
        if user["username"] == username :
            if user["age"] >= 18 and user["active"] == True :
                return True
        
    return False 



            

users = [{ "username": "ali","age": 25,"city": "Tehran","active": True },
     {"username": "sara","age": 17,"city": "Tabriz","active": True},
     {"username": "fatemeh","age": 35,"city": "Esfehan","active": True},
     {"username": "maryam","age": 19,"city": "Hamedan","active": False},
     {"username": "roya","age": 30,"city": "ghazvin","active": True},
     {"username": "amin","age": 37,"city": "Ardebil","active": False}]
check = check_access(users, "fatemeh")
print(check)


"""
False 

"""


#-----------------------------------------d---------------------------------------


def get_adult_users(users : list) -> list :
    """
    SUMMARY : tabee baraye ezafe kardan afrade balaye 18 sal be yek list jadid.

    Parameters
    ----------
    users : list
        DESCRIPTION : vorodi.

    Returns
    -------
    list
        DESCRIPTION : khoroji listi az afrad balaye 18 sal ast.
    """
    
    adult_list = []
    for user in users :
        if user["age"] >= 18 :
            adult_list.append(user)
            
    return adult_list
            



users = [{ "username": "ali","age": 25,"city": "Tehran","active": True },
     {"username": "sara","age": 17,"city": "Tabriz","active": True},
     {"username": "fatemeh","age": 35,"city": "Esfehan","active": True},
     {"username": "maryam","age": 19,"city": "Hamedan","active": False},
     {"username": "roya","age": 30,"city": "ghazvin","active": True},
     {"username": "amin","age": 37,"city": "Ardebil","active": False}]
check = get_adult_users(users)
print(check)


"""
[{'username': 'ali', 'age': 25, 'city': 'Tehran', 'active': True},
 {'username': 'fatemeh', 'age': 35, 'city': 'Esfehan', 'active': True},
 {'username': 'maryam', 'age': 19, 'city': 'Hamedan', 'active': False},
 {'username': 'roya', 'age': 30, 'city': 'ghazvin', 'active': True}, 
 {'username': 'amin', 'age': 37, 'city': 'Ardebil', 'active': False}]

"""







