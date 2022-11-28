def even_infinite():
    num=0
    while num<4:
        yield num
        num+=2
even_iter_obj=even_infinite() 
for i in range(2)   :
    next(even_iter_obj)      
print(next(even_iter_obj ))    

 