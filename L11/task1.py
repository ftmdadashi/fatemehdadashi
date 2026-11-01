"""

task1: system modiroiat vasayele naghliyeh.

farz konid sherkati baraye modiriat vasayele naghliye khod be yek system

narmafzari niyaz darad. in sherkat daraye khodrohaye benzini va electrici ast.

har 2 no vasileye naghliye vizhegihaye moshtaraki darand, ama raveshe mohasebeye

hazine safar da aan ha motefavet ast.
_________________________________________________________________
bakhshe aval: class valed Vehicle

class ba vizhegihaye brand, model, year va distance_traveled tarahi konid.

method haye zir ra piyadeh sazi konid:
    
___ show_info() baraye namayeshe etelaate vasayele naghliye.

___ drive(distance) baraye afzayeshe masafate tey shode, ba baresi mosbat boodane voroodi.

___ calculate_trip_cost(distance) ke dar class valed ba NotEmplementedError

moshakhas mikonad mohasebe bayad dar kodam class farzand piyadeh sazi shavad.
__________________________________________________________________
bakhshe dovom: class haye farzand

__class GasCar ra az Vehicle ers bari dahid.

in class bayad vizhegihaye:
    
fuel_consumption: masrafe litr dar 10 Km va fuel_price dashte bashad va 

hazineye safar ra barasase masrafe benzin mohasebe konad.

__ class ElectricCar niz az vehicle ers bari mikonad va daraye enrgy_consumption

Kw/h dar 100 km va electricity_price mibashad.

dar har 2 class ba super() etelaate moshtarak ra meghdar dehi konid va methode

calculate_trip_cost() ra baznevisi konid.
__________________________________________________________________
bakhshe sevom: ejraye barname

hadeaghal 4 abject az 2 no khodro besazid, aan hara dar yek List negahdari konid

va ba yek halghe, etelaat va hazine safar 150 Km har kodam ra namayesh dahid.

nemon estefade morede entezar:
    
car1 = GasCar()
car2 = ElectricCar()
vehicles = [car1,car2]
for vehicle in vehicles:
    vehicle.show_info()
print(vehicle.calculate_trip_cost(150))

"""

class Vehicle:
    def __init__(self,brand,model,year,distance_traveled):
        self.brand = brand
        self.model = model
        self.year = year
        self.distance_traveled = distance_traveled
        
        
    def show_info(self):
        print("________________your car information_______________________")
        print(f"band:{self.brand}, model:{self.model}, year:{self.year}")
        
        
        
    def drive(self,distance):
        if distance < 0 :
            raise ValueError("distance should be positive.")
            
        else :
            self.distance_traveled += distance
            return f"Your distance traveled is :{self.distance_traveled}"
    
    
    def calculate_trip_cost(self,distance):
        raise NotImplementedError("You shoud use Gas/Electric class for calculating trip cost.")
        
        
    def __str__(self):
        print("This class uses for car's information.")
        
        
        
class GasCar(Vehicle):
    def __init__(self,brand,model,year,distance_traveled,fuel_consumption,fuel_price):
        super().__init__(brand,model,year,distance_traveled)
        self.fuel_consumption = fuel_consumption
        self.fuel_price = fuel_price
        
        
    def calculate_trip_cost(self,distance):
        trip_cost = (distance/100) * self.fuel_consumption * self.fuel_price
        return f"Your cost for trip is : {trip_cost}"
    
    
    def __str__(self):
        return f" Your GASCAR has fuel consumption :{self.fuel_consumption}"\
                f" and fuel price :{self.fuel_price}"





class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, distance_traveled,energy_consumption,energy_price):
        super().__init__(brand, model, year, distance_traveled)
        self.energy_consumption = energy_consumption
        self.energy_price = energy_price
        
       
    def calculate_trip_cost(self,distance):
        trip_cost = (distance/100) * self.energy_consumption * self.energy_price
        return f"Your cost for trip is : {trip_cost}"
    
    
    def __str__(self):
        return f" Your ELECTRICCAR has energy consumption :{self.energy_consumption}"\
                f" and energy price :{self.energy_price}"




car1 = GasCar("BMW", "X4", 2022, 15000, 8, 30000)
car2 = GasCar("Mercedes-Benz", "C-Class", 2023, 10000, 9, 30000)

car3 = ElectricCar("Tesla", "Model3", 2024, 5000, 18, 2000)
car4 = ElectricCar("Audi", "GT", 2023, 8000, 20, 2000)


vehicles = [car1,car2,car3,car4]
for vehicle in vehicles :
    vehicle.show_info()
    print(vehicle.calculate_trip_cost(150))




"""

________________your car information_______________________
band:BMW, model:X4, year:2022
Your cost for trip is : 360000.0
________________your car information_______________________
band:Mercedes-Benz, model:C-Class, year:2023
Your cost for trip is : 405000.0
________________your car information_______________________
band:Tesla, model:Model3, year:2024
Your cost for trip is : 54000.0
________________your car information_______________________
band:Audi, model:GT, year:2023
Your cost for trip is : 60000.0


"""















