"""



Q11----Mohasebe Soode foroshe mahsool
ma yek listi darim az gheymate kharide mahsoolat , va yek listi darim az ghyemate foroshe mahsoolat
shoma bayad soode har kodom az mahsoollat ro dar yek liste jodagane hesab konid


buy_prices = [100, 200, 150, 400]
sell_prices = [130, 250, 190, 500]


"""


buy_prices = [100, 200, 150, 400]
sell_prices = [130, 250, 190, 500]
profit = []


for i in range(4):
     pro = sell_prices[i] - buy_prices[i]
     profit.append(pro)
        


print("your buy_prices is : ",buy_prices)
print("your sell_prices is : ",sell_prices)        
print("your profit is : ",profit)





"""

khoroji :
    

your buy_prices is :  [100, 200, 150, 400]
your sell_prices is :  [130, 250, 190, 500]
your profit is :  [30, 50, 40, 100]


"""    
