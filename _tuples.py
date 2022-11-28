marks=int(input("enter your marks::"))
if (marks>=90 and marks<=100):
    print('you score execelent') 
elif (marks>=80 and marks<=90):
    print('you score a grade')    
elif (marks>=70 and marks<=80):
    print('you score b grade')    
elif (marks>=60 and marks<=70):
    print('you score c grade')  
elif (marks>=50 and marks<=60):
    print('you score d grade')  
elif (marks<50):
    print('you score f grade')   
else:
    print("You are fail")  