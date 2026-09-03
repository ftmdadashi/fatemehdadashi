"""

2 - yek listi az nomre haye daneshjoha va esmashon dairm, dar enteha faghat

esme daneshjohaei ke pass shodan ro neshon bede (optional : onaro rank bandi ham kone)

students = ['ali','vahid','sara','hamid','reza','elham','mohsen','zahra','paniz','parmida']
scores = [20,17,9 , 13, 7 , 20 , 18 , 3 , 1 , 14]


"""



students = ['ali','vahid','sara','hamid','reza','elham','mohsen','zahra','paniz','parmida']
scores = [20,17,9 , 13, 7 , 20 , 18 , 3 , 1 , 14]
passed_dic = {}
rank = 1


for name,num in zip(students,scores) :
    if num >= 10 :
        print(name,"with score",num,"is passed.")
        passed_dic[name] = num
        
    

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

        
while passed_dic :
    
    max_score = list(passed_dic.values())[0]
    
    
    for scores in passed_dic.values():
        if scores >= max_score :
            max_score = scores
            
            
    for name,scores in passed_dic.items() :
        if scores == max_score :
            print(rank,":",name,"with score",max_score)
            break
        
        
    passed_dic.pop(name)
    rank += 1
    
    
    
"""

dar in barname ebteda tamami afrad ba nomre pas shode dar dakhele yek

dictionary gharraa migirand, sepas avalin value ra be onvane maximum

dar nazar migirim va bad ba baghiye addad moghayese mishvad,

agar bozorgtarin adda dar miyan adda basha be onvvan max dar nazar gerefteh shode 

va hamrah ba name aan az dictionary hazf mishavad, va in halghe ta enteha bar

rooye dictionary edame peyda mikonad ta dictionary khali shavad.


khoroji :
    

    ali with score 20 is passed.
    vahid with score 17 is passed.
    hamid with score 13 is passed.
    elham with score 20 is passed.
    mohsen with score 18 is passed.
    parmida with score 14 is passed.
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    1 : ali with score 20
    2 : elham with score 20
    3 : mohsen with score 18
    4 : vahid with score 17
    5 : parmida with score 14
    6 : hamid with score 13

"""
        
        
        
        
        
        
        
            
