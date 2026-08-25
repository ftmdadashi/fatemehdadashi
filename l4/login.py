"""


Q1----- Login 

az User , usernamesh ro begirid va passwordesh ro ham begirid , agar
username barabar bashe ba admin va password bashe 1234 nenevesidi Login ba moafaghiat
anajm shod, agar na , benevisid password ya username ghalat hast.


"""


username = input("please enter your username :").strip()
password = input("please enter your password :")

if username == "admin" and password == "1234":
    print("Ba moafaghiat anjam shod")
    
else :
    print("password ya username ghalat hast")
    
    
    
    
"""

khoroji :
    
please enter your username :    admin
please enter your password :1234
Ba moafaghiat anjam shod




please enter your username :    fatemeh
please enter your password :1234
password ya username ghalat hast


"""