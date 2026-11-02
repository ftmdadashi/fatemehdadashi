"""

system foroshgah va mohasebeye hazineye ersal

yek foroshgah internety mikhahd mahsoolate digital va physicy khod ra modiriat konad.

in tamrin edameye ideh Product dar jalaseye 11 ast, ba in tafavot ke bayad yek 

system monsajem tarai shavad.

________________________________________________________________________
bakhsh aval: class Product

vizhegihaye code, name, price, stock va sell_count ra tarif konid.

method haye show(), sell(quantity), restock(quantity), apply_discount(percentage) va 

is_available() ra piyadeh sazi konid.

ghavanin: forosh bishtar az mojodi mojaz nist, tedade forosh ya afzayeshe mojodi

bayad mosbat bashad va darsade takhfif bayad beyne sefr ta 100 gharar begirad.

________________________________________________________________________
bakhshe dovom: class Location

class ba vizhegihaye address, x va y besazid va methode calculate_distance(other_location) 

ra baraye mohasebeye faseleye oghlidosi do mogheiat piyadeh sazi konid.

ba isinstance() etminan hasel konid ke voroodi yek object az noe Location ast.

________________________________________________________________________
bakhshe sevom: class haye farzand

class DigitalProduct az Product ers bari mokonad va vizhegiye download_link

va methode get_download_link() dashte bashad.

class PhysicalProduct niz az Product ers bari mikonad va daraye weight va 

warehouse_location bashad.baraye mohasebeye hazineye ersal methode zir ra 

piyadeh sazi knid:
    
calculate_shipping(destination)

formoole mohasebe:
    
ShippingCost = Distance\times weight\times 1000

mogheiat anbar va maghsade bayad object haee az class Location bashand.

_________________________________________________________________________
bakhshe cheharom: azmoone barname

hadagal do mahsool digital va do mahsoole physicy va do mogheiate makani besazid .

sepas forosh, afzayesh mojoodi, takhfif, mohaebe fasele va hazne ersal ra azmayesh

konid.

"""
import math


class Product:
    def __init__(self,code,name,price,stock):
        self.code = code
        self.name = name
        self.price = price
        self.stock = stock
        self.sell_count = 0
        
        
        
    def show(self):
        print("_______________Your product information________________")
        print(f"Name:{self.name}, Code:{self.code}, Price:{self.price}")
        
        
    def sell(self,quantity):
        if quantity < 0 :
            raise ValueError("Quantity should be positive.")
            
        if quantity > self.stock:
            raise ValueError("Quantity can't be more than stock.")
            
        self.sell_count += quantity
        self.stock -= quantity
        
        
        
    def restock(self,quantity):
        if quantity < 0 :
            raise ValueError("Quantity should be positive.")
            
        self.stock += quantity
        
        
    def apply_discount(self,percentage):
        if percentage > 100 or percentage < 0 :
            raise ValueError("Percentage should be between [0,100].")
            
        self.price -= self.price * (percentage/100)
        return f"Your finall price after discount is:{self.price}"
        
        
    def is_available(self):
        if self.stock>0:
            return True 
        else:
            return False
        
        
    def __str__(self):
        return f'{self.code}:{self.name}'
        
        

class Location:
    def __init__(self,address,x_cordinate,y_cordinate):
        self.address = address
        self.x_cordinate = x_cordinate
        self.y_cordinate = y_cordinate
        
        
    def calculate_distance(self,other_location):
        if not isinstance(other_location, Location) :
            raise NotImplementedError("location should be from class Location.")
            
        x_distance = other_location.x_cordinate - self.x_cordinate
        y_distance = other_location.y_cordinate - self.y_cordinate
        
        distance = math.sqrt( ((x_distance **2) + (y_distance **2)))
        return distance
    
    
    def show(self):
        print("_______________Your product' address information________________")
        print(f"Name:{self.name}, Code:{self.code}, address:{self.address}")
        
     
    
    

class DigitalProduct(Product):
    def __init__(self, code, name, price, stock,download_link):
        super().__init__(code, name, price, stock)
        self.download_link = download_link
        
        
    def get_download_link(self):
        return f"Your download link is : {self.download_link}"
    
    
    def show(self):
        print("_______________Your DigitalProduct information________________")
        print(f"Name:{self.name}, Code:{self.code}, download_link:{self.download_link}")
        
     
        
        
        
class PhysicalProduct(Product):
    def __init__(self, code, name, price, stock,weight,address,x,y):
        super().__init__(code, name, price, stock)
        self.weight = weight
        self.warehouse_location = Location(address = address, x_cordinate = x, y_cordinate = y)
        self.price_per_mass_meter = 1000

        
    def calculate_shipping(self,destination):
        if not isinstance(destination, Location):
            raise NotImplementedError("location should be from class Location.")
            
        distance = self.warehouse_location.calculate_distance(destination)
        cost = distance * self.weight * self.price_per_mass_meter
        return cost
 
    
      
    def show(self):
        print("_______________Your PhysicalProduct information________________")
        print(f"Name:{self.name}, Code:{self.code}, wight:{self.weight}")
        
     
    
        
product1 = DigitalProduct("z11"," ML book", 1200000, 3 , "www.skybook.com/ml")   
product2 = DigitalProduct("z12", "IT book", 1300000, 5, "www.skybook.com/it") 

product1.sell(5)    #ValueError: Quantity can't be more than stock.
product2.sell(2)
product2.stock      #Out[11]: 3
product1.restock(3)
product1.stock      #Out[13]: 6
product2.apply_discount(20)     #Out[20]: 'Your finall price after discount is:1040000.0'
      
    
#____________________________________________________________________________

product3 = PhysicalProduct("a1", "TV", 20000000, 5,10, "satarkhan", 400 , -200)
product4 = PhysicalProduct("a2", "washing_machine",40000000,10, 30, "shahrara", 400, -300)


product3_base_location = Location("satarkhan", 400, -200)
product3_finall_location = Location("shariati", 400, -150)

product3.calculate_shipping(product3_finall_location)    #Out[45]: 500000.0












