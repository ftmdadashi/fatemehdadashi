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


    
#jomle , kalame
sentence='i love python and i love deep learning'
#(sentence,love)

sentence.count('love') #Out[53]: 2


def count_word(sentence,word):
    count = sentence.count(word)
    return count 

#ba for

def count_word(sentence,myword):
    count = 0 
    senetnce_list = sentence.split()
    for word in senetnce_list:
        if word == myword:
            count = count + 1  
    return count 

    










