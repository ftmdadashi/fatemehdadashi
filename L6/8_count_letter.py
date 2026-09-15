"""

# 8_count_letter.py

yek tabe benevisid ke do khoroji begire, yek kalame va yek horof , var bere beshmore chand
ta oon harf dakhele oon kalame hast va oon adad ro khoroji bede.

do bar tabe ro benevisid

a) faghat az for estefade konid

b) az for esteafde nakonid


"""


#-------------------------------------a------------------------------------------



def count_letter_for(word :str , char :str) -> int :
    """
    SUMMARY : tabe made nazar char morede nazar ra dar word peyda karde
    va tedade aan ra mishmorad.

    Parameters
    ----------
    word : str
        DESCRIPTION : word avalin vorodi.
    char : str
        DESCRIPTION : char dovomin vorodi.

    Returns
    -------
    int
        DESCRIPTION :dar enteha tedade char be onvane khoroji barmigardad.
    """
    count = 0

    for i in word :
        if i == char :
            count += 1
            
    return count
            


count_char = count_letter_for("fatemehdadashi", "a")
print("your char repeats :", count_char)



"""
your char repeats : 3

"""




#-------------------------------------b------------------------------------------



def count_letter(word :str , char :str) -> int :
    """
    SUMMARY : tabe made nazar char morede nazar ra dar word peyda karde
    va tedade aan ra mishmorad.

    Parameters
    ----------
    word : str
        DESCRIPTION : word avalin vorodi.
    char : str
        DESCRIPTION : char dovomin vorodi.

    Returns
    -------
    int
        DESCRIPTION :dar enteha tedade char be onvane khoroji barmigardad.
    """
    
    count = word.count(char)
    return count


count_char = count_letter("fatemehdadashi", "a")
print("your char repeats :", count_char)


"""
your char repeats : 3

"""













