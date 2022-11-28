a={1,2,3,4,1}#repetation not allowed
print(type(a))
print(a)

k=set()
print(type(k))
k.add(77)
k.add(("abc"))
print(k)
a.add((88,55,88,96))
print(a)
print(len(a))
a.remove(3)# removal of item
print(a)

print(a.pop())
print(a.clear())
print(a.union({3,5,8,9,9,6,66,7}))


#write a programme to input eight number from the user and display all the unique number
a=int(input("Enter no1::"))
b=int(input("Enter no2::"))
c=int(input("Enter no3::"))
d=int(input("Enter no4::"))
e=int(input("Enter no5::"))
f=int(input("Enter no6::"))
g=int(input("Enter no7::"))
h=int(input("Enter no8::"))
abc={a,b,c,d,e,f,g,h}
print(abc)





p=set()
p.add(20)
print(p)
p.add(20.0)
p.add("20")
print(len(p))




f={}
print(type(f))


#creat a empty dictonary allow 4 friends to enter their name as key and their language as values and names are unique
u={}
a=input("Enter your Favorite Language subham\n")
b=input("Enter your Favorite Language ankit\n")
c=input("Enter your Favorite Language ram\n")
d=input("Enter your Favorite Language sham\n")
u['subham']=a
u['ankit']=b
u['ram']=c
u['sham']=d
print(u)


