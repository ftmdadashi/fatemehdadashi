"""


Q12---- Gereftane mahsool

ba estefade az halgheye for , yek systemi benevisid , ke 5 bar az karbar esme yek
mahsool begire (masalan zara, nike ,..) va agar toole oon mahsool kamtar az 6 bashad
dakhele yek listi bename sabade_kharid berizad.



"""


sabade_kharid = []


for i in range(5) :
    product = input("please enter your product 's name :")
    if len(product) < 6 :
        sabade_kharid.append(product)
        
        
        
    
print("sabade_kharid =",sabade_kharid)





"""

khoroji :
    

please enter your product 's name :dior
please enter your product 's name :fendi
please enter your product 's name :prada
please enter your product 's name :chanel
please enter your product 's name :gucci
sabade_kharid = ['dior', 'fendi', 'prada', 'gucci']


"""