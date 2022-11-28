f=open("sample.txt", "r")
data=f.readline()
print(data)
data=f.readline()
print(data)
data=f.readline()
print(data)
data=f.readline()
print(data)
data=f.readline()
print(data)
f.close()



#r===>open for reading
#w===> open for writing
#a==>open for appending
#+===>open for updating
k=open("__anothertxt.txt",'w')#####Here to creat a .txt File
k.write("please write this to file")
k.write("i am appending")
 
k.close()