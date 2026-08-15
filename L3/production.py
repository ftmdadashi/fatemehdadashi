"""

q3.5. az karbar esme product ro begire berize to zarf

gheymatesho begire berize too zarf

code takhfif begire

age code takhfif barabar bood ba z14

20% az gheymat kam kone nmaayesh bede
bege gheymate nahaei ine 


q3.5.2. --> ag code takhfif eshtebah zad --> bege 
ghalat zadid

q3.5.3 --> ag ghalat zad, bege yekbar dg mitoni emtehan kone
ag doros zad anjam bde (takhfif) ag na --> bege block shodid




"""

product_name = input("Please enter your product name :")
product_price = float(input("Please enter your produt price :"))
product_discount_code = input("Please enter your product discount code :")

if product_discount_code == "z14" :
    product_discount = product_price * 0.2
    finall_price = product_price - product_discount
    print("Your",product_name," finall price is :", finall_price)
    
else :
    print("Ghalat zadid")
    print("-----------Yekbare digar emtehan konid---------------- ")
    product_discount_code = input("Please enter your product discount code :")

    if product_discount_code == "z14" :
        product_discount = product_price * 0.2
        finall_price = product_price - product_discount
        print("Your", product_name,"finall price is :", finall_price)

    else :
        print("block shodid")
    



"""

khoroji chenin ast:
    
%runfile F:/python/3_class/session03/production.py --wdir
Please enter your product name :KAFSH
Please enter your produt price :12000
Please enter your product discount code :Z12
Ghalat zadid
-----------Yekbare digar emtehan konid---------------- 
Please enter your product discount code :Z14
block shodid

%runfile F:/python/3_class/session03/production.py --wdir
Please enter your product name :kafsh
Please enter your produt price :12000
Please enter your product discount code :z12
Ghalat zadid
-----------Yekbare digar emtehan konid---------------- 
Please enter your product discount code :z14
Your kafsh finall price is : 9600.0


"""
















