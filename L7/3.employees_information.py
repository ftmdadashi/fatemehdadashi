"""

3. kar ba etelaate karmandan.

yek tabe benevisid ke yek dict az karmandan va etelaate anha ra be onvane

vorodi daryaft konad.

employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },
    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },
    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}

1. esme fardi ke balatarin hoghogh ra migirad, bargardande shavad.
2. esme fardi ke kamtarin hoghogh ra migirad, bargardande shavad.
3. yek list az esme afradi ke hoghoghe balaye 3000 migirand, bargardande shavad.
4. tabe do vorodi begirad, yek, hamin dict va dovomi yek adad . dar khoroji list 
esme afradi ke hoghogheshan bishtar az aan adad ast ra bargardanad.
5. miangine kole hoghogh ha ra bargardanad.

"""

#---------------------------------------1-----------------------------------------------


def find_name_most_price(employees : dict) -> str :
    """
    SUMMARY : dar yek dict az information karmandan, mikhahim fardi ba 
    bishtarin hoghogh ra peda konim.

    Parameters
    ----------
    employees : dict
        DESCRIPTION : vorodi tabe yek dict az information karmandan ast.

    Returns
    -------
    str
        DESCRIPTION : khoroji tabe name aan fard ast.
    """
    
    
    for information in employees.values() :
        maximum_salary = information["salary"]
        maximum_salary_name = information["name"]
        break
    
    
    for information in employees.values() :
        if information["salary"] > maximum_salary :
            maximum_salary = information["salary"]
            maximum_salary_name = information["name"]
            
    return maximum_salary_name




employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },
    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },
    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}


check = find_name_most_price(employees)
print(check, "has the most salay in dictionary of information.")
#Sara has the most salay in dictionary of information.


#-----------------------------------------2---------------------------------------------


def find_name_least_price(employees : dict) -> str :
    """
    SUMMARY : tabee ke name fard ba kamtarin hoghogh ra barmigardanad.

    Parameters
    ----------
    employees : dict
        DESCRIPTION : vorodi tabe.

    Returns
    -------
    str
        DESCRIPTION : khoroji tabe ke name yek fard ba kamtarin hoghogh ast.
    """
    
    
    for information in employees.values() :
        minimum_price = information["salary"]
        minimum_price_name = information["name"]
        break
    
    
    for information in employees.values():
        if information["salary"] < minimum_price :
            minimum_price = information["salary"]
            minimum_price_name = information["name"]
            
    return minimum_price_name
    
    


employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },
    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },
    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}


check = find_name_least_price(employees)
print(check, "has the least salay in dictionary of information.")
#Reza has the least salay in dictionary of information.


#-----------------------------------3-------------------------------------------------------


def name_list_most_price(employees :dict) -> list :
    """
    SUMMARY : tabe ee baraye tashkhise afrsd ba hoghoghe balaye 3000.

    Parameters
    ----------
    employees : dict
        DESCRIPTION : vorodi tabe.

    Returns
    -------
    list
        DESCRIPTION : listi az afradi ke hoghoghe balaye 3000 darand.
    """
    
    
    name_list = []
    for information in employees.values() :
        if information["salary"] > 3000 :
            name_list.append(information["name"])
            
    return name_list
    



employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },
    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },
    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}


check = name_list_most_price(employees)
print("These employees have salary more than 3000 :", check)



#--------------------------------------4----------------------------------------------


def find_name(employees : dict , number : int) -> list :
    """
    SUMMARY : tabe ee baraye peyda kardane afradi ba hoghoghe balatar az 
    number.

    Parameters
    ----------
    employees : dict
        DESCRIPTION : vorodi aval.
    number : int
        DESCRIPTION: vorodi dovom.

    Returns
    -------
    list
        DESCRIPTION: listi az afrad ba hoghoghe bala tar az number.
    """
    
    
    name_list = []
    for information in employees.values() :
        if information["salary"] > number :
            name_list.append(information["name"])
            
    return name_list        
    
            
    
employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },
    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },
    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}
    
    
check = find_name(employees, 2900)
print("name_list =" ,check)   #name_list = ['Ali', 'Sara']
    
    
#-------------------------------------5------------------------------------------------

def average_of_salary(employees : dict) -> float :
    """
    SUMMARY : tabe ee baraye miangine salary ha.

    Parameters
    ----------
    employees : dict
        DESCRIPTION : vorodi aval.

    Returns
    -------
    float
        DESCRIPTION : khoroji az type float .
    """
    
    
    total = 0 
    for information in employees.values() :
        total += information["salary"]
        
    average = total / len(employees)
    return round(average , 2)
    #round moshakhas mikonad ta chand ragham ashar bekhorad.




   
employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },
    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },
    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}



check = average_of_salary(employees)
print("The average of salaries is :", check) 
  #The average of salaries is : 3433.33
























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








