def even_number(n:int) :
    for number in range(2,n,2) :
        yield number
        
        
        
check = even_number(80)
print(next(check))   #2
print(next(check))   #4
print(next(check))   #6
        

