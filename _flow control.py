#read two numberfrom keyboard and find who is big and which is smaller
a=eval(input('enter two numbers:::::'))
b=eval(input('enter two numbers:::::'))
c=eval(input('enter two numbers:::::'))
if a>b and a>c:
    print('a is greater than b and c','and value of a is',a)
elif b>c:
    print('b is greatre than a and c',"and  value of b is",b)
else:
    print('c is greatre than a and b',"and  value of c is",c)    









# read the input is in between 0 to 100
number=eval(input("enter the value:::::::::"))
if 0<number<100:
    print('the number is in between  0 to 100',number)
elif number==0:
    print("The number is in between the range",number) 
else:
    print('The number is out of 0 TO 100',number)

      



#please enter singel digit number
num=eval(input("enter the value::::"))
if num==0:
    print("value is zero",num)
elif num==1:
    print("value is one",num)    
elif num==2: 
    print("value is two",num) 
elif num==3:
    print("value is three",num)
elif num==4:
    print("value is four",num)
elif num==5:
    print("value is five",num)
elif num==6: 
    print("value is six",num) 
elif num==7:
    print("value is seven",num)
elif num==8:
    print("value is eight",num)
elif num==9:
    print("value is nine",num) 
else:
    print('sorry please enter a single digit number',"your enter number is not valid",num)
                        