

from curses.ascii import isalnum, isalpha


s="Durga"
print("g" in s)
print("o" in s)




k=input("Enter Main string:::")
sub=input("Entre substring to search::")
if sub in k:
    print(sub,"is found in Main string")
else:
    print(sub,"is not found in main string")    



    #Cmparision Operator
 #   >,>=,<=
  #  equality operators
 # a----->97

 # A------>65

# "durga"    'durga'
# "durga"    'naseer'






s1=input("Enter First String::")
s2=input("enter second  string::")
if s1==s2:
    print("Both are equal")
elif s1>s2:
    print(" s1 is greater")
else:        
    print('s2 is greater')


l1=["a","b","c"]
l2=["a","b","c"]
l3=l2
print(id(l1))
print(id(l2))
print(l3 is l2)    
print(l1 == l2)


city=input('Enter Your city Name::::')
list=['Hydrabad',"bengaluru",'Delhi',"Mumbai",'Pune']
if city.strip() in list:
    print("Service is avalible in your City",city,"come in Time")
else:
    print("Please Enter valid city",city,'is not avalible in list')    


#   lstrip() delete space beginging of the string
#   rstrip() delete space last of string
#     strip() delete space
#replace
s='Learning Python is very difficult'
print(s)
s=s.replace('difficult','easy')
print(s)



s="aaaabbbbabbaababababbabbabababa"
print(s)
s=s.replace('a','b')
print(s)
print(len(s))




s="bababbababababab"
s1=s.replace('a','b')
print(s,"adress is::",id(s))
print(s1,"Adress is",id(s1))

#splitting

s="Durga Software Solution" 
print(s)



s="02-03-2018"
l=s.split('-')
for x in l:
    print(x)



g="1 2 3 4 5 6 7 8 9 0"
f=g.rsplit(" ")
for x in f:
    print(x)

y="Himansu"
d=y.split('i' and 'a')
for t in d:
    
    print(t)   
    print("\n") 




s="Durga softwear solutions Hyd India"    
l=s.split(' ',4)
for x in l:
    print(x)



t="H I M A N S U"
h=t.split(" ",100)
for j in h:
    print(j)




o='abababaababaujfuufuf  '
g=o.rsplit(" ")
for k in g:
    print(k)
    



#join
t=("abc",'def','ghi')    
j=":::".join(t)
print(j)

#changing case of a string
#---------------------------
#upper()==>To convert upper case
#lower()==>To convert lower case
#swapcase()==>Swap case
#title()==>The Python Clases By Durga  Sir
#capitalize()==>The python clases by durga  sir





s="The Python Clases By Durga  Sir"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())

#strats and ends with
#------------------
s="The Python Clases By Durga  Sir"
print(s.startswith('The'))
print(s.endswith('Sir'))




#______________________________________
#============================================
##isalnum()==>only alphanumeric character a-z,A-Z,0-9
#isalpha()==>only alphabet
#isdigit()==>only 








y="Durga789"
print(y.isalnum())
print(y.isdigit())
print(y.islower())
print(y.isupper())
print(y.isalpha())
print(y.istitle())





s=input("Enter some character:::")
if s.isalnum():
    print("Alpha numeric character")
    if s.isalpha():
        print("alphabatic character")
        if s.islower():
            print('lowercase alphabatic character')
        else:
            print("uppercase alphabatic character")
    else:
        print("it is a digit")
elif s.isspace():
    print('it is space character')
else:
    print('Non space character')  
##format
#@____________________

name="Durga"
age=48
salary=10000

print("{a}'s Age is{b} and his salary is{c}".format(a=name,b=age,c=salary))



#reverse
s=input('enter some string:')

for x in reversed(s):
    print(x,end=" ")

s=input("Enter Some String:")
i=len(s)-1
output=""
while i>=0:
    output=output+s[i]
    i=i-1
print(output)   





#input=abc def ghi
#output=ghi def abc
s=input('enter some string::')
l=s.split()
l1=[]
i=len(l)-1
while i>=0:
    l1.append(l[i])
    i=i-1
output="".join(l1) 
print(output)   

# input=abc def ghi 

# output= cba fed ihg
s=input("Enter some string:")
l=s.split()
l1=[]
for x in l:
    l1.append(x[::-1])

output='  '.join(l1)
print(output)
#IN
s1="RAVITEJA"
S2="SOFT"





#Q9. Write a program to remove duplicate characters from the given input string?
#input: ABCDABBCDABBBCCCDDEEEF
#output: ABCDEF
s=input('enter some string:::')
l=[]
for x in s:
    if x not in l:
        l.append(x)
output=" ".join(l)
print(output)        





#Write a program to perform the following activity
#input: a4k3b2
#output:aeknbd
s=input('Enter some stering:')
output=''
for i in s:
    if i.isalpha():
         print("jh")