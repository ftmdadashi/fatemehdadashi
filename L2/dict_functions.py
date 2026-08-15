"""

yek file besazid bename dict_functions.py , yek dictionaruy besazid az 
etelaate khodeton mesle esm , reshte tahsil , va .. va az tabe haye
dictionary estefade konid

"""

dic_1 = {"name":"faemeh", "family":"dadashi" , "date of birth": "21 april 1991"
         , "B.sc": "applied methematics", "B.sc university": "kharazmi",
         "M.sc":"It (E-Commerce)", "M.sc university": "K.N.Toosi"}


dic_1.clear()

print(dic_1)

"""

tamami dic ra pak karde va yek dic khali barmigardanad.

khoroji:
    
{}

"""


dic_1 = {"name":"faemeh", "family":"dadashi" , "date of birth": "21 april 1991"
         , "B.sc": "applied methematics", "B.sc university": "kharazmi",
         "M.sc":"It (E-Commerce)", "M.sc university": "K.N.Toosi"}


dic_1.copy()

print(dic_1)

"""

yek copy az dic migirad.

khoroji :
    
{'name': 'faemeh', 'family': 'dadashi', 'date of birth': '21 april 1991',
 'B.sc': 'applied methematics', 'B.sc university': 'kharazmi',
 'M.sc': 'It (E-Commerce)', 'M.sc university': 'K.N.Toosi'}

"""


a = {"ghad", "vazn"}

dic_2 = dict.fromkeys(a)

print(dic_2)


"""

in tabe bar asase key haye jadid baraye ma dic jadid misaze, chon value ha 

moshakhas nist, br jashon None mizare.

khoroji:
    
{'vazn': None, 'ghad': None}

"""

dic_1 = {"name":"faemeh", "family":"dadashi" , "date of birth": "21 april 1991"
         , "B.sc": "applied methematics", "B.sc university": "kharazmi",
         "M.sc":"It (E-Commerce)", "M.sc university": "K.N.Toosi"}


b = dic_1.get("date of birth")

print(b)


"""

baraye dastresi be yek value, kafi ast ke Key marboot be aan neveshteh shavad.

khoroji :
    
21 april 1991

"""


dic_1 = {"name":"faemeh", "family":"dadashi" , "date of birth": "21 april 1991"
         , "B.sc": "applied methematics", "B.sc university": "kharazmi",
         "M.sc":"It (E-Commerce)", "M.sc university": "K.N.Toosi"}


c = dic_1.items()

print(c)


"""

ba estefade az itemm mitavan, dictionary marboot ra be yek list az tuple

tabdil kard, ke dastresi be Key ha ra sadeh tar mikonad.

khoroji :
    
dict_items([('name', 'faemeh'), ('family', 'dadashi'),
            ('date of birth', '21 april 1991'), 
            ('B.sc', 'applied methematics'), 
            ('B.sc university', 'kharazmi'),
            ('M.sc', 'It (E-Commerce)'), 
            ('M.sc university', 'K.N.Toosi')])

"""



dic_1 = {"name":"faemeh", "family":"dadashi" , "date of birth": "21 april 1991"
         , "B.sc": "applied methematics", "B.sc university": "kharazmi",
         "M.sc":"It (E-Commerce)", "M.sc university": "K.N.Toosi"}

d = dic_1.keys()

print(d)


"""

dar in ravesh, tamamie key haye dictionary be sorate list bargardande mishavad.

khoroji :
    
dict_keys(['name', 'family', 'date of birth',
           'B.sc', 'B.sc university', 'M.sc', 
           'M.sc university'])    
    
    
"""    



dic_1 = {"name":"faemeh", "family":"dadashi" , "date of birth": "21 april 1991"
         , "B.sc": "applied methematics", "B.sc university": "kharazmi",
         "M.sc":"It (E-Commerce)", "M.sc university": "K.N.Toosi"}


e = dic_1.pop("date of birth")

print(e)


"""

ba estafade az in method value e marboot be key made nazar hazf mishavad.

banabarin agar aan ra pop konim az dictionary hazf shode ( ham value 
                                                          
va ham key hazf mishavad) va be onvane  moteghayer jadide 

sakhte shode barmigardad.


khoroji :
    
21 april 1991

"""

dic_1 = {"name":"faemeh", "family":"dadashi" , "date of birth": "21 april 1991"
         , "B.sc": "applied methematics", "B.sc university": "kharazmi",
         "M.sc":"It (E-Commerce)", "M.sc university": "K.N.Toosi"}

f = dic_1.popitem()

print(f)


"""

akharin item marboot be dictionary ra hazf karde va be sorate tuple

barmigardanad.

khoroji :
    
('M.sc university', 'K.N.Toosi')

"""


dic_1 = {"name":"faemeh", "family":"dadashi" , "date of birth": "21 april 1991"
         , "B.sc": "applied methematics", "B.sc university": "kharazmi",
         "M.sc":"It (E-Commerce)", "M.sc university": "K.N.Toosi"}


g = dic_1.setdefault("M.sc", "Information Technology")

print(g)


"""

dar in method value marboot be key made nazar ("M.sc") bayad bargardande shavad

agar aan key vojod nadasht banabarin ("Information Technology") bargardande 

mishavad.

khoroji :
    
It (E-Commerce)

"""



dic_1 = {"name":"faemeh", "family":"dadashi" , "date of birth": "21 april 1991"
         , "B.sc": "applied methematics", "B.sc university": "kharazmi",
         "M.sc":"It (E-Commerce)", "M.sc university": "K.N.Toosi"}


h = dic_1.update({"name":"atena"})

print(dic_1)


"""

baraye update kardane dictionart estefade mishavad.

khoroji :
    
{'name': 'atena', 'family': 'dadashi', 'date of birth': '21 april 1991',
 'B.sc': 'applied methematics', 'B.sc university': 'kharazmi',
 'M.sc': 'It (E-Commerce)', 'M.sc university': 'K.N.Toosi'}

"""


dic_1 = {"name":"faemeh", "family":"dadashi" , "date of birth": "21 april 1991"
         , "B.sc": "applied methematics", "B.sc university": "kharazmi",
         "M.sc":"It (E-Commerce)", "M.sc university": "K.N.Toosi"}

h = dic_1.values()

print(h)


"""

dar in ravesh tamami value ha be sorate list bargardande mishavand.

khoroji :
    
dict_values(['faemeh', 'dadashi', '21 april 1991', 'applied methematics',
             'kharazmi', 'It (E-Commerce)', 'K.N.Toosi'])

"""





