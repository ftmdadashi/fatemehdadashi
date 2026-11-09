"""
system modiriat karbaran ba file va class

dar jalaseye 11 yad gereftim chegoneh etelaate karbaran ra dakhele file matni

negah dari konim va ba tavabe va class ha anha ra modiriat konim. aknon mikhahim

in system ra kameltar va ghabel estefade tar bekonim.

sakhtar file: users.txt

ali|12345|ali@gmil.com|active
sara|abc789|sara@gmail.com|active
reza|45678|reza@gmail.com|blocked

in ramzhaye mtni faghat baraye tamrine file khani hastand, dar barname vaghee 

ramz oobor bayad be soorate hash shode zakhireh shavad.

___________________________________________________________________________
bakhshe aval: class User

vizhegihaye email, address, password, username, statu ra dashte bashad.

2 methode zir ra piyadehsazi konid:
    
___ to_format() ke etelaat karbar ra be format yak khat az file tabdil konad.

___ ___str__() ke namayeshe khanaee mesle User:ali tolid konad.


_____________________________________________________________________________
bakhshe dovom: class FileManager

class bayad name file ra dar zaman sakht daryaft konad.

method haye zir ra piyadeh sazi konid:
    
  method                                 task
------------                     ----------------------------
    
read_users()                         khandan file va sakhte listi az object haye User
find_user(username)                  jostojoye karbar va bargardandane object
add_user()                           ezafe kardane karbar e jadid
delete_user(username)                hazfe karbar az file
update_status(username,status)       taghire vaziat active/blocked
login(username,password)             baresi etelaat vorood
generate_roport()                    namayesh tedad karbaran faal va masdood


ghavanine barname:
    
1. name karbari tekrari nabayad sabt shavad.
2. karbaran masdood nabayad betavanand vared shavand.
3. dar sorate naboodane file, barname bayad ba modiriate khata an ra ijad konad
va ya vaziat monasebi gozaresh dahad.
4. bad az hazf ya taghire vaziat karbar, etelaat bayad vaghean dar file zakhireh shavand.
5. khandan chanbare file nabayad karbaran tekrari dar list dakheli ijad konad.

___________________________________________________________________________
bakhshe sevom: mwnu ye barname

yek menu sade ba while tarahi konid:
    
========================USER MNAGEMENT=====================================

1. ADD USER
2. FIND USER
3. DELETE USER
4. UPDATE STATUS
5. LOGIN
6. GENERATE REPORT
7. EXITE

"""


class User:
    def __init__(self, username, password, email, status):
        self.username = username
        self.password = password
        self.email = email
        self.status = status

    def to_format(self):
        formatted_name = f'{self.username}|{self.password}|{self.email}|{self.status}\n'
        return formatted_name

    def __str__(self):
        return f"User : {self.username}"


class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.users = []
        self.active_account = 0
        self.blocked_account = 0
        self.numbers_of_users = 0

    def read_users(self):
        self.users.clear()

        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    words = line.strip().split("|")
                    username = words[0]
                    password = words[1]
                    email = words[2]
                    status = words[3]

                    if not self.find_user(username):
                        user = User(username, password, email, status)
                        self.users.append(user)

        except FileNotFoundError:
            print("file does not exist.")



    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return False
    
    

    def add_user(self, username, password, email, status):
        if self.find_user(username):
            return False

        if status not in ["active", "blocked"]:
            return False

        new_user = User(username, password, email, status)
        formatted_text = new_user.to_format()

        with open(self.file_name, 'a') as file:
            file.write(formatted_text)

        self.users.append(new_user)
        return True
    
    

    def delete_user(self, username):
        if self.find_user(username):
            return False
        
        for user in self.users:
            if user.username == username:
                self.users.remove(user)

        with open(self.file_name, "w") as file:
            for user in self.users:
                formatted_text = user.to_format()
                file.write(formatted_text)

        return True
    
    
    

    def update_status(self, username, status):
        if status not in ["active", "blocked"]:
            return False
        
        if self.find_user(username):
            return False
       
        for user in self.users:
            if user.username == username:
                user.status = status

        with open(self.file_name, "w") as file:
            for user in self.users:
                formatted_text = user.to_format()
                file.write(formatted_text)

        return True
    
    
    
    

    def login(self, username, password):
        user = self.find_user(username)

        if not user:
            return False

        if user.status == "blocked":
            return False

        if user.password == password:
            return True

        return False
    
    
    

    def generate_roport(self):
        self.numbers_of_users = 0
        self.active_account = 0
        self.blocked_account = 0

        for user in self.users:
            self.numbers_of_users += 1

            if user.status == "active":
                self.active_account += 1
            else:
                self.blocked_account += 1

        return (
            f"total numbers of user is :{self.numbers_of_users}, "
            f"{self.active_account} of them are active and "
            f"{self.blocked_account} of them are blocked."
        )


check = FileManager("users.txt")


print("===============USER MANAGEMENT==================")
print("1. ADD USER")
print("2. FIND USER")
print("3. DELETE USER")
print("4. UPDATE STATUS")
print("5. LOGIN")
print("6. GENERATE REPORT")
print("7. EXIT")

massage = input("Choose an option...")

while massage != "7":

    if massage == "1":

        username = input("Enter username: ")

        password = input("Enter password: ")

        email = input("Enter email: ")

        status = input("Enter status: ")

        result = check.add_user(username, password, email, status)

        print(result)

    elif massage == "2":

        username = input("Enter username: ")

        result = check.find_user(username)

        print(result)
        

    elif massage == "3":

        username = input("Enter username: ")

        result = check.delete_user(username)

        print(result)

    elif massage == "4":

        username = input("Enter username: ")

        status = input("Enter new status: ")

        result = check.update_status(username, status)

        print(result)

    elif massage == "5":

        username = input("Enter username: ")

        password = input("Enter password: ")

        result = check.login(username, password)

        print(result)

    elif massage == "6":

        result = check.generate_roport()

        print(result)

    else:

        print("Invalid option!")

    massage = input("Choose an option...")

print("you want to exit!")      
        
        
        
        
        
                

            

        
        
        
                
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    