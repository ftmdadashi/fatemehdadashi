"""

yek barname modirat karbaran tarahi konid ke etelaat ra dakhele file user.txt

zakhireh konad.

sakhtar e etelaat :
    
1,Ali,ali@gmail.com,active
2,Sara,sara@gmail.com,blocked
3,Reza,reza@gmail.com,active

tavabe morede niyaza:
    
1. add_user() ezafe kardane karbar jadid ba shenase, name, email, vaziat.

2. find_user() peyda kardane karbar barasase shenase ya name.

3. delete_user() hazfe karbar barasase shenase.

4. update_user() tagheer email va ya vaziat karbar.

5. list_users() namayeshe tamame karbaran.

6. generate_report() namayeshe tedad karbaran faal, masdood va tedade kole karbaran.


"""




def add_user(user_id: int, name: str, gmail: str, status: str):
    """
    SUMMARY : this function is used to add new user in file.

    Parameters
    ----------
    user_id : int
        DESCRIPTION : first input
    name : str
        DESCRIPTION : second input
    gmail : str
        DESCRIPTION : third input
    status : str
        DESCRIPTION : fourth input

    Returns
    -------
    None
    """
    
    information_list = []

    try:
        with open("user.txt", "r") as f:
            for line in f:
                words = line.strip().split(",")

                information_dict = {
                    "user_id": int(words[0]),
                    "name": words[1],
                    "gmail": words[2],
                    "status": words[3]
                }

                information_list.append(information_dict)

    except FileNotFoundError:
        print("file does not exist.")

    for user in information_list:
        if user["user_id"] == user_id and user["name"] == name:
            print("User exists.")
            return

    information_dict = {
        "user_id": user_id,
        "name": name,
        "gmail": gmail,
        "status": status
    }

    information_list.append(information_dict)

    with open("user.txt", "w") as f:
        for user in information_list:
            f.write(
                f"{user['user_id']},{user['name']},"
                f"{user['gmail']},{user['status']}\n"
            )



print("1. continue")
print("2. exit")
massage = input("Do you want to continue ...?")
while massage != "2" :
    user_id = int(input("please enter user_id:"))
    name = input("please enter name:")
    gmail = input("please enter gmail:")
    status = input("please enter status:")
    add_user(user_id, name, gmail, status)
    massage = input("Do you want to continue ...?")



 #1,Ali,ali@gmail.com,active
 #2,Sara,sara@gmail.com,blocked  
 #3,Reza,reza@gmail.com,active

            
            
#--------------------------------------------------------------------------------


def find_user(user_id:int,name:str) :
    """
    SUMMARY : this function is used to find special user.

    Parameters
    ----------
    user_id : int
        DESCRIPTION : first input
    name : str
        DESCRIPTION : second input

    Returns
    -------
    str
        DESCRIPTION : returns the information dictionary of special user.  
    """
    
    
    information_list = []
    try :
        with open("user.txt","r") as f:
            for line in f :
                words = line.lower().strip().split(",")
                information_dict = {
                    "user_id": int(words[0]),
                    "name": words[1],
                    "gmail": words[2],
                    "status": words[3]
                }
    
                information_list.append(information_dict)
    except FileNotFoundError :
        print("file does not exist.")

                   
            
            
    for user in information_list :
        if user["user_id"] == user_id and user["name"] == name :
            return f"your user is :{user['user_id']},{user['name']},{user['gmail']},{user['status']}"
        
         

print("1. continue")
print("2. exit")
massage = input("Do you want to continue ...?")
while massage != "2" :
    user_id = int(input("please enter user_id:"))
    name = input("please enter name:")
    check = find_user(user_id, name)
    print(check)
    massage = input("Do you want to continue ...?")


#Out[35]: 'your user is :1,Ali,ali@gmail.com,active'
            
            
#--------------------------------------------------------------------------------



def delete_user(user_id:int) :
    """
    SUMMARY : this function is used to delete a special user.

    Parameters
    ----------
    user_id : int
        DESCRIPTION : input

    Returns
    -------
    None
    """
    
    
    information_list = []
    try :
        with open("user.txt","r") as f:
            for line in f :
                words = line.lower().strip().split(",")
                information_dict = {
                    "user_id": int(words[0]),
                    "name": words[1],
                    "gmail": words[2],
                    "status": words[3]
                }
    
                information_list.append(information_dict)
    except FileNotFoundError :
        print("file does not exist.")
        
        
    for user in information_list :
        if user["user_id"] == user_id :
            information_list.remove(user)
            break
        
    with open("user.txt","w") as f :
        for user in information_list :
            f.write(f"{user['user_id']},{user['name']},{user['gmail']},{user['status']}\n")
    
    
            
 

print("1. continue")
print("2. exit")
massage = input("Do you want to continue ...?")
while massage != "2" :
    user_id = int(input("please enter user_id:"))
    check = delete_user(user_id)
    print(check)
    massage = input("Do you want to continue ...?")
           
 
             
    

    


"""
delete_user(1)

"""



#-----------------------------------------------------------------------------------


def update_user(name:str,gmail:str,status:str) :
    """
    SUMMARY : this function is used to upadte gmail or status based on name.

    Parameters
    ----------
    name : str
        DESCRIPTION : first input
    gmail : str
        DESCRIPTION : second input
    status : str
        DESCRIPTION : third input

    Returns
    -------
    None
    """
   
    information_list = []
    try :
        with open("user.txt","r") as f:
            for line in f :
                words = line.lower().strip().split(",")
                information_dict = {
                    "user_id": int(words[0]),
                    "name": words[1],
                    "gmail": words[2],
                    "status": words[3]
                }
    
                information_list.append(information_dict)
    except FileNotFoundError :
        print("file does not exist.")
        
    for user in information_list :
        if user["name"] == name :
            user["gmail"] = gmail
            user["status"] = status
            break
        
    with open("user.txt","w") as f :
        for user in information_list :
            f.write(f"{user['user_id']},{user['name']},{user['gmail']},{user['status']}\n")
    
    


print("1. continue")
print("2. exit")
massage = input("Do you want to continue ...?")
while massage != "2" :
    name = input("please enter name:")
    gmail = input("please enter your gmail :")
    status = input("please enter your status :")
    check = update_user(name, gmail, status)
    print(check)
    massage = input("Do you want to continue ...?")





#------------------------------------------------------------------------------------



def list_users() :
    """
    SUMMARY : this function is used to return a list containing 
    dictionaries of users information.

    Returns
    -------
    TYPE : list
        DESCRIPTION : a list of information.
    """
    
    
    
    information_list = []
    try :
        with open("user.txt","r") as f:
            for line in f :
                words = line.lower().strip().split(",")
                information_dict = {
                    "user_id": int(words[0]),
                    "name": words[1],
                    "gmail": words[2],
                    "status": words[3]
                }
    
                information_list.append(information_dict)
    except FileNotFoundError :
        print("file does not exist.")
        
        
    return information_list
    




print("1. continue")
print("2. exit")
massage = input("Do you want to continue ...?")
while massage != "2" :
    check = list_users()
    print(check)
    massage = input("Do you want to continue ...?")





#-------------------------------------------------------------------------------------


def generate_report() :
    """
    SUMMARY : this function is used to generate information about status and
    total numbers of users.

    Returns
    -------
    str
        DESCRIPTION : the numbers of users, blocked and active numbers.
    """
    
    
    information_list = []
    try :
        with open("user.txt","r") as f:
            for line in f :
                words = line.lower().strip().split(",")
                information_dict = {
                    "user_id": int(words[0]),
                    "name": words[1],
                    "gmail": words[2],
                    "status": words[3]
                }
    
                information_list.append(information_dict)
    except FileNotFoundError :
        print("file does not exist.")
        
    
    active_account = 0
    blocked_account = 0
    numbers_of_users = 0
    
    for user in information_list :
        numbers_of_users += 1
        
        if user["status"] == "active" :
            active_account += 1
            
        else :
            blocked_account += 1 
            
    return f"total numbers of user is :{numbers_of_users}, {active_account} of them are active and "\
           f"{blocked_account} of them are blocked."
    





print("1. continue")
print("2. exit")
massage = input("Do you want to continue ...?")
while massage != "2" :
    check = generate_report()
    print(check)
    massage = input("Do you want to continue ...?")




#-------------------------------------------------------------------------------------












            
            
            

            
    