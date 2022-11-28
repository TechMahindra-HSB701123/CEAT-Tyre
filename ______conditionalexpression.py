





num=int(input("Enter The Number:::"))
u=1
for i in range(1,num+1):
    u=u*1
print(f"The factorial is{num} is{u} ")  

n=3
for i in range(3):
    print(" " * (n-i-1),end='')
    print("*" * (2*i+1),end=" ")
    print(" " * (n-i-1))