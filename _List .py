
a=[1,2,3,4,5]
print(a)
print(a[2])
print(a[-2])
l=a[3]=98
print(l)
print(a)




#list slicing
l=[45,'abc','Himansu',]
print(l[0:2])


#list method
#sort
l1=[1,8,7,2,21,15]
print(l1)
l1.sort()
print(l1)
#reverce
l1.reverse()
print(l1)
#append
l1.append(456)
print(l1)
l1.append(789)
print(l1)
l1.insert(4,11111)
print(l1)
#pop
l1.pop(3)
print(l1)
#remove
l1.remove(15)
print(l1)




#by user input 7 fruits
f1=input("enter fruit Number 1")
f2=input("enter fruit Number 2")
f3=input("enter fruit Number 3")
f4=input("enter fruit Number 4")
f5=input("enter fruit Number 5")
f6=input("enter fruit Number 6")
f7=input("enter fruit Number 7")
MyFruitList=[f1,f2,f3,f4,f5,f6,f7]
print(MyFruitList)
MyFruitList.sort()
print(MyFruitList)


#student
m1=int(input("enter fruit Number 1"))
m2=int(input("enter fruit Number 2"))
m3=int(input("enter fruit Number 3"))
m4=int(input("enter fruit Number 4"))
m5=int(input("enter fruit Number 5"))
m6=int(input("enter fruit Number 6"))
student=[m1,m2,m3,m4,m4,m5,m6]
print(student)
student.sort()
print(student)




#summ in list
l=[10,5,77,32]
print(l[0]+l[1]+l[2]+l[3])
print(sum(l))

#count number of zero in tuple
a=(7,0,8,0,0,9)
z=a.count(0)
print(z)
