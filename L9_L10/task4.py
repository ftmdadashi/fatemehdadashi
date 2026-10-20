"""

yek class be name product tarahi konid ke moshakhasate mahsoolat yek froshgah

ra modiriat konad. har mahsool bayad daraye vizhegihaye zir bashad ;

name
price
quantity
category

method haye morede niyaz:
    
1. __init__() meghdar dehi avaliyeh vizhegihaye mahsool.

2. __str__() namayesh khana va moratabe moshakhasate mahsool.

3. update_price() taghire gheymate mahsool.

4. add_stock() afzayeshe mojoodi.

5. sell() froshe tedad moshakhasi az mahsool va kam shodane mojodi.

6. apply_discount() emale takhfife darsadi.

7. total_value() mohasebe arzeshe kole mojoodi yek mahsool.

nemoneh nahveh estefade:
    
p1 = Product("Laptop",50000000,5,"Electronics")
print(p1)
p1.sell(2)
p1.apply_discount(10)
p1.add_stock(3)
print(p1.total_value())

ghavanin:
    
gheymat nemitavanad manfi bashad.
mojoodi nabayad kamtar az sefr bashad.
takhfif bayad beyne 0 ta 100 bashad.
agar mojoodi kafi nabood, amaliat frosh nabayad anjam shavad.

chaleshe ezafe :
    
chand object az class Product besazid, dakhele yek list negah dari konid va

mahsool ba bishtarin arzeshe mojodi ra peyda konid.

"""

class Product :
    
    def __init__(self,name:str,price:float,quantity:int,category:str) :
        if price < 0 :
            raise ValueError("price can't be negative.")
        else :
            self.price = price
        self.name = name
        self.quantity = quantity
        self.category = category



    def __str__(self) :
        
        return f"{self.quantity} of {self.name} with price:{self.price} "\
            f" and category :{self.category} is available."
            
            
    def update_price(self,new_price) :
        
        if new_price < 0 :
            raise ValueError("price can't be negative.")
        else : 
            self.price = new_price
            
            
    def add_stock(self,quantity) :
        
        if quantity <= 0 :
            raise ValueError("quantity can't be negative.")
        else :
            self.quantity += quantity


    def sell(self,quantity) :
        
        if quantity <= 0 :
            raise ValueError("quantity can't be negative or zero.")
        elif quantity > self.quantity :
            raise ValueError("quntity can't be more than available quantity")
        else :
            self.quantity -= quantity
                
            
    def apply_discount(self,percentage) :
        
        if percentage > 100 or percentage < 0 :
            raise ValueError("percentage should be in available range.")
        else :
            self.price -= self.price * (percentage/100)
        
        
    def total_value(self) :
        total_price = self.price * self.quantity
        return total_price
        

    
p1 = Product("Laptop",50000000,5,"Electronics")
print(p1)      #5 of Laptop with price:50000000 and category :Electronics is available.
p1.sell(2)
p1.apply_discount(10)
p1.add_stock(3)
print(p1.total_value())      #270000000.0



#--------------------------------chalesh-------------------------------------------

p1 = Product("Laptop",50000000,5,"Electronics")
p2 = Product("Rice", 1200000, 30, "Food")
p3 = Product("Novel", 350000, 12, "Books")
p4 = Product("Sneakers", 2800000, 7, "Clothing")
p5 = Product("Perfume", 6200000, 10, "Beauty")
p6 = Product("basketball", 900000, 15, "Sports")
p7 = Product("Headphones", 1800000, 20, "Electronics")
p8 = Product("Chocolate", 250000, 40, "Food")
p9 = Product("watch", 8500000, 3, "Accessories")
p10 = Product("lipgloss", 1200000, 9, "beauty")


objects_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
count = 0
for p in objects_list :
    count += 1
    print(count,":",p)


"""

1 : 5 of Laptop with price:50000000  and category :Electronics is available.
2 : 30 of Rice with price:1200000  and category :Food is available.
3 : 12 of Novel with price:350000  and category :Books is available.
4 : 7 of Sneakers with price:2800000  and category :Clothing is available.
5 : 10 of Perfume with price:6200000  and category :Beauty is available.
6 : 15 of basketball with price:900000  and category :Sports is available.
7 : 20 of Headphones with price:1800000  and category :Electronics is available.
8 : 40 of Chocolate with price:250000  and category :Food is available.
9 : 3 of watch with price:8500000  and category :Accessories is available.
10 : 9 of lipgloss with price:1200000  and category :beauty is available.

"""

price_list = []
for p in objects_list :
    price_list.append(p.price*p.quantity)

maximum__stock_price = max(price_list)    
for p in objects_list :   
    if p.price * p.quantity == maximum__stock_price :
        maximum_price_name = p.name
        print(f"{maximum_price_name} : {maximum__stock_price} is the most expensive product...")


#Laptop : 250000000 is the most expensive product...




















