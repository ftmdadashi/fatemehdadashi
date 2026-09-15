"""

# 1_calculate_age.py

Dar in file shoam bayad yek tabe (function) benevisid ke yek vorodi begire (sale tavalod) va sen 
ro hesb kone va sen ro khoroji bede . 

a ) hamin soal hast ke vorodi fght sale tavalod hast

b ) yek tabe digar besazid do vorodi begire, sale tavalod va tarikh . tarikh agar miladi bod 
besorate miladi hesab kone agar shamsi bood shamsi hesab kone.  yani be tabe masalan 
bedim (1377,'shamsi') ya inke bedim (1999,'miladi')

c) hamoon tabeye (b) ro benevisid , agar tabe fght yek vorodi gereft , be sorate 
pish farz miladi dar nazar begire


d) tabe ro begone ei benevisid ke fght yek vorodi begire yani fght tarikh , ama khodesh 
betone tashkhis bede k miladi user dade ya shamsi (hint : range ro check koni )

"""




#------------------------------------a------------------------------------------

def birth(year:int)->int :
    """
    SUMMARY : tabee baraye mohasebe sen barasase sale tavalod.

    Parameters
    ----------
    year : int
        DESCRIPTION : sale tavalod be onvane vorodi.

    Returns
    -------
    int
        DESCRIPTION : sen be onvane khoroji mibashad.
    """
    
    age = 1405 - year
    return age
    

your_age = birth(1370)
print("your age is :",your_age)



"""
your age is : 35

"""



#------------------------------------b------------------------------------------

def birth_year(year:int , calender:str)-> int :
    """
    SUMMARY : tabe baraye mohasebe sen barasase sale shamsi ya miladi ast.

    Parameters
    ----------
    year : int
        DESCRIPTION : sale tavalod ba type int vorodi mibashad.
    calender : str
        DESCRIPTION : sale shamsi ya miladi ba type str vorodi dovom mibashad.

    Returns
    -------
    int
        DESCRIPTION : age khoroji tabe mibashad.
    """
    
    if calender == "miladi":
        age = 2026 - year
        return age
    
    elif calender == "shamsi" :
        age = 1405 - year
        return age
    
    else :
        raise ValueError ("your data is INVALID.")
        
        
        
your_age = birth_year(1370, "shamsi")
print("your age is :",your_age)

your_age = birth_year(1991, "miladi")
print("your age is :", your_age)    
    


"""

your age is : 35
your age is : 35

"""




#------------------------------------c------------------------------------------


def birth_special_year(year:int , calender:str = "miladi" ) -> int :
    """
    SUMMARY : tabe mohasebe sen

    Parameters
    ----------
    year : int
        DESCRIPTION : sale tavalod be onvan vorodi aval.
    calender : str
        DESCRIPTION. The default is "miladi".

    Returns
    -------
    int
        DESCRIPTION : age be onvan khoroji mibashad.

    """
    
    
    if calender == "shamsi" :
        age = 1405 - year
        return age
    
    else :
        age = 2026 - year
        return age        
    
    

your_age = birth_special_year(1991)
print("yout age is :", your_age)


"""

yout age is : 35

"""



#------------------------------------d------------------------------------------

def birth_date(year:int)->int :
    """
    SUMMARY : tabe tashkhis sen az tarighe sale tavalod.

    Parameters
    ----------
    year : int
        DESCRIPTION :sale tavalod be onvane vorodi .

    Returns
    -------
    int
        DESCRIPTION : age be onvane khoroji mibashad .
    """
    
    if year < 1406 :
        age = 1405 - year
        return age
    
    else :
        age = 2026 - year
        return age
    

    
your_age = birth_date(1330)
print("your age is :",your_age)


"""

your age is : 75


"""

