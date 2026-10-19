"""

barnamee tarahi konid ke masire yek pooshe ra az karbar daryaft konad va etelaat 

e file haye mojood dar aan ra tahlil konad.

baraye mesal, pooshee ba file haye zir darim:
    
    
       project
       \
       \
       \------------main.py
       \
       \
       \------------users.txt
       \
       \
       \------------report.pdf
       \
       \
       \------------image.jpg
       \
       \
       \------------data.csv
       
       
ghabeliathaye morede niyaz :
    
1. barresi vojod e pooshe ba estefade az os.

2. namayeshe name tamame file haye mojood dar pooshe.

3. mohasebe tedad file ha.

4. mohasebe hajme har file bar hasbe KB.

5. mohasebe majmo va miangine hajme file ha.

6. peyda kardane bozorgtarin va kochektarin file.

7. estefade az math.ceil() baraye gerd kardane hajme file ha  be adade sahihe balatar.

8. shomareshe file ha barasase pasvand masle .py ya .txt .

chaleshe ezafe :

ba estefade az os yek poshe be name reports ijad konid va gozaresh tahlil ra 

dar yek file matni dakhele aan zakhireh konid.

--nokteh-- da bakhshe asli tamrin faghat file haye mostaghim dakhele pooshe barresi shavand

va barresi zirpoosheha ekhtiyari ast.

"""

#---------------------------------------1--------------------------------------------


import os



path = input("please enter your path :")
print(os.path.exists(path))


"""
please enter your path :F:\python\project
True

"""

#----------------------------------------2-------------------------------------------




user_path = input("please enter your path :")
print(os.path.exists(user_path))

files_name = os.listdir(user_path)
print("the name of files :",files_name)


"""

please enter your path :F:\python\project
True
the name of files : ['data.csv', 'image.jpg', 'main.py', 'report.pdf', 'users.txt']

"""

#-----------------------------------------3-------------------------------------------



user_path = input("please enter your path :")
print(os.path.exists(user_path))

files_numbers = len(os.listdir(user_path))
print("the name of files :",files_numbers)


"""

please enter your path :F:\python\project
True
the name of files : 5

"""


#----------------------------------------4----------------------------------------



user_path = input("please enter your path :")

for file in os.listdir(user_path) :
    files_size = os.path.getsize(user_path) /1000
    print(f"{file} size is :{files_size}")



"""
please enter your path :F:\python\project
data.csv size is :4.096
image.jpg size is :4.096
main.py size is :4.096
report.pdf size is :4.096
users.txt size is :4.096

"""


#-----------------------------------5---------------------------------------------


file_size_list = []
user_path = input("please enter your path :")

for file in os.listdir(user_path) :
    files_size = os.path.getsize(user_path) /1000
    file_size_list.append(files_size)


sum_of_size = sum(file_size_list)
average = sum_of_size / len(file_size_list)
print(f"sum of the sizes is :{sum_of_size} and average is : {average}")

"""
please enter your path :F:\python\project
sum of the sizes is :20.48 and average is : 4.096

"""


#-----------------------------------6--------------------------------------------


file_size_list = []
user_path = input("please enter your path :")

for file in os.listdir(user_path) :
    files_size = os.path.getsize(user_path) /1000
    file_size_list.append(files_size)


maximum_size = max(file_size_list)
minimum_size = min(file_size_list)

print(f"maximum size is :{maximum_size} and minimum is :{minimum_size}")


"""
please enter your path :F:\python\project
maximum size is :4.096 and minimum is :4.096

"""

#------------------------------------7-------------------------------------------

import math

file_size_list = []
user_path = input("please enter your path :")

for file in os.listdir(user_path) :
    files_size = os.path.getsize(user_path) /1000
    files_size = math.ceil(files_size)
    file_size_list.append(files_size)
    print(f"{file} size is :{files_size}")



"""

please enter your path :F:\python\project
data.csv size is :5
image.jpg size is :5
main.py size is :5
report.pdf size is :5
users.txt size is :5

"""

#------------------------------------8--------------------------------------------



user_path = input("please enter your path :")
format_file_list = []
for file in os.listdir(user_path) :
    name_file = os.path.splitext(file)
    format_file = name_file[1]
    format_file_list.append(format_file)
    
print(format_file_list)
    
"""
please enter your path :F:\python\project
['.csv', '.jpg', '.py', '.pdf', '.txt']
"""

format_dict = {}
for form in format_file_list :
    if form in format_dict.values() :
        format_dict[form] += 1
        
    else :
        format_dict[form] = 1
        
        
print(format_dict)    #{'.csv': 1, '.jpg': 1, '.py': 1, '.pdf': 1, '.txt': 1}
        

#---------------------------------chalesh------------------------------------------


import math

path = r"F:\python\reports"
os.mkdir(path)

user_path = input("please enter your path :")

with open(r"F:\python\reports\report.txt" , "w") as f :
    files_name = os.listdir(user_path)
    f.write(f"the name of files :{files_name}\n")
    
        
    
    files_numbers = len(os.listdir(user_path))
    f.write(f"the name of files :{files_numbers}\n")
    
        
    for file in os.listdir(user_path) :
        files_size = os.path.getsize(user_path) /1000
        f.write(f"{file} size is :{files_size}\n")
    
        
    
    file_size_list = []
    
    for file in os.listdir(user_path) :
        files_size = os.path.getsize(user_path) /1000
        file_size_list.append(files_size)
    
    
    sum_of_size = sum(file_size_list)
    average = sum_of_size / len(file_size_list)
    f.write(f"sum of the sizes is :{sum_of_size} and average is : {average}\n")
    
    
    
    for file in os.listdir(user_path) :
        files_size = os.path.getsize(user_path) /1000
        file_size_list.append(files_size)
    
    
    maximum_size = max(file_size_list)
    minimum_size = min(file_size_list)
    
    f.write(f"maximum size is :{maximum_size} and minimum is :{minimum_size}\n")
    
    
    
    file_size_list = []
    
    for file in os.listdir(user_path) :
        files_size = os.path.getsize(user_path) /1000
        files_size = math.ceil(files_size)
        file_size_list.append(files_size)
        f.write(f"{file} size is :{files_size}\n")
    
    
    
    
    format_file_list = []
    for file in os.listdir(user_path) :
        name_file = os.path.splitext(file)
        format_file = name_file[1]
        format_file_list.append(format_file)
        
    f.write(f"{format_file_list}\n")
        
    format_dict = {}
    for form in format_file_list :
        if form in format_dict.values() :
            format_dict[form] += 1
            
        else :
            format_dict[form] = 1
            
            
    f.write(f"{format_dict}\n")
    
    
    
    
  
    
    
    
    
    
    
    
    



































