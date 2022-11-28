#list
s={10,20,30,10,20,30}
print(s)
#print(s[2]) # not support indexing/sliceing/subscriptable
print(s.add(555))
print(s.add("Himansu"))
print(s)




##a,b,c,d={int(x) for x in input('enter 2 numbers:').split()}
#print(a+b+c+d)
#print('the product:',a*b**b/c-d)



#k,l,j=(float(x) for x in input('enter 2 float value:').split(":"))
#print("k+l+j::::",k+l+j)


ex=input('enter some expression:::')
result=eval(ex)
print('The result:',result)