#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6

for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")



n=(1,2,3,4,5,6,7,8,9)
counteven=0
countodd=0
for x in n:
    if x%2==0:
        counteven=counteven+1
        
    else:
       countodd=countodd+1    
print("no of even number",counteven)      
print("no of odd are",countodd) 