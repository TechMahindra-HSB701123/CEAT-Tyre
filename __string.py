s="""durga
softwear
solution"""
print(s)




s='''The python class" by 'durga sir' is good'''
print(s)





#mathematical operator
i='durga'+' sai'
print(i)
print('durga '*5)
print(len('Durga'))



d=input("Enter some string::::")
n=len(d)
i=0
print("data in forward direction")
while i<n:
    print(s[i],end='')
    i=+1
print("data in backward direction")
while i>n:
    print(s[i],end="")
    i=i+1  




s=input("Enter some string::")    
print("Even position are",s[::2])
print("odd positions are",s[1::2])
i=0
print("the character at even position::")
while i<len(s):
    print(s[i],end=',')
    i+=2
print()
print("The Character at odd position are::") 
i=1
while i<len(s):
    print(s[i],end=":::")
    i+=2



s=input("Enter some string::")   
s1=s2=output=''
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x           
print(s1)
print(s2)
print(output)        



k="abhdy154462695dknndv"
x=sorted(k)
print(x)




s=input("Enter some string::")
output=''
for x in s:
    if x.isalpha():
        output+=x
        previous=x
    else:
        output=output+previous*x-1   
print(output) 



#input=a4k3b2
#output=aeknbd
s=input("Enter some string::")
output=''
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        newch=chr(ord(previous)+int(x))
        output=output+newch
print(output)        

