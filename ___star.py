
n=4
for i in range(70000000):
    print("*"*(i+1))


n=3
for i in range(3):
    print(" " * (n-i-1),end='')
    print("*" * (2*i+1),end=" ")
    print(" " * (n-i-1))
    
#print multiplication table in reverse order
num=int(input("Enter The Number:::"))
for i in range(1,11):
    print(f'{num}*{i}={num*i}')




num=int(input("Enter The Number:::"))

for i in range(11):
    print(num*i)


# sum of number


num=int(input("Enter The Number:::"))
for i in range(101):
    print(f"{num}+{i}={num+i}")