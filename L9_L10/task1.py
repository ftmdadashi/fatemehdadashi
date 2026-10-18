"""

farz konid masoole sabte nomarate yek kelas hastid. barnamee benevisid ke 

nomarate daneshjoyan ra daryaft kardeh va dar filee be name grades.txt 

zakhireh konad.

har khat e file bayad be sorate zir bashad.

Ali, 18.5

Sara, 16

Reza, 19.25

ghabeliathaye morede niaz :
    
1. tabe add_grade() baraye daryaft name va nomreh daneshjoo va zakhireh aan dar file.

2. tabe read_grades() baray khandan va namayaeshe nomarat.

3. tabe calculate_average() baraye mohasebe miangine class.

4. tabe find_top_student() baraye peyda kardane daneshjoye daraye bishtarin nomreh.

5. estefade az try/except baraye modiriat khatahaee manande vared kadrane

matn be jaye nomreh, nomre kharej az mahdodoeh 0 ta 20 , naboodane file va

dadehaye namotabar.


-----chalesh jadid : ejazeh nadahid baraye yek daneshjoo 2 nomreh sabt shavad.

baraye sabte nomre jadid, nomre ghabli be rozresani shavad.

"""




def add_grade(name : str , grade : float) :
    """
    SUMMARY : this function is used to add a user.

    Parameters
    ----------
    name : str
        DESCRIPTION : name is a first input .
    grade : float
        DESCRIPTION : grade is second input.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        DESCRIPTION : this error occurs when file does not exist.
    """
    
    try :
        info_dict = {}
        if isinstance(name, str) :
            if isinstance(grade, (int,float))  :
                if  0<= grade <= 20 :
                    
                    try:    
                        with open("grades.txt","r") as f :
                            for line in f :
                                words = line.strip().split(",")
                                info_dict[words[0]] = float(words[1])
                                
                    except FileNotFoundError :
                        pass
                                
                    info_dict[name] = grade
                        
                    with open("grades.txt","w") as f :
                        for name , grade in info_dict.items():
                            if name in info_dict.keys():
                                info_dict[name] = grade
                                f.write(f"{name},{grade}\n")

                                
                            else :
                                f.write(f"{name},{grade}\n")
            
                        
                      
                else :
                    raise ValueError("you should enter number on range 0-20")
                        
            else :
                raise ValueError("you shoud enter int/float as a number.")
        else :
            raise ValueError("you should enter str as a name")
            
    except ValueError as e :
        print(e)        


add_grade("ali",18.5)
add_grade("sara",16)
add_grade("reza",19.25)
add_grade("ali", 17)


"""
ali,17
sara,16.0
reza,19.25

"""


#-----------------------------------------------------------------


def read_grades() :
    """
    SUMMARY : this function is used to read grades.

    Returns
    -------
    TYPE
        DESCRIPTION : returns a list of grades.
    """
    
    
    grades = []
    with open("grades.txt","r") as f :
        for lines in f :
            word = lines.strip().split(",")
            grades.append(float(word[1]))            
        return grades  
            
    
 
read_grades()         #Out[72]:Out[8]: [17.0, 16.0, 19.25]


#-------------------------------------------------------------------


def calculate_average() :
    """
    SUMMARY : this function is used to calculate average of numbers.

    Returns
    -------
    None
    """
    
    
    grades = read_grades()
    average = sum(grades) / len(grades)
    average = round(average,2)
    print("The average of grades is :", average)
             
             

calculate_average()     #The average of grades is : 17.42
    
    
#--------------------------------------------------------------------


def find_top_student() :
    """
    SUMMARY : this funcion is used to find top student.

    Returns
    -------
    TYPE
        DESCRIPTION : returns the name of top student.
    """
    
    
    information_dict = {}
    with open("grades.txt","r") as f :
        for line in f :
            words = line.split(",")
            information_dict[words[0]] = float(words[1])
        
        top_student = max(information_dict,key=information_dict.get)
        return top_student
    
    

find_top_student()             #Out[79]: 'reza'


#-------------------- rahe dovom   ------------------------------




def find_top_student() :
    
    information_dict = {}
    with open("grades.txt","r") as f :
        for line in f :
            words = line.split(",")
            information_dict[words[0]] = float(words[1])
        
        max_grade = max(information_dict.values())
        for name, grade in information_dict.items() :
            if max_grade == grade :
                top_student = name
        return top_student
    
    

find_top_student()             #Out[79]: 'reza'













