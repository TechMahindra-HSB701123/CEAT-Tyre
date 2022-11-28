with open('sample.txt')as f:
    content=f.read().lower()
if "harry" in content:
    print('yes harry is present')
else:
    print('no harry is not present') 



    ##################line number   



content=True
i=1
with open("poem.txt")as f:
    while content:
        content=f.readline()
        if 'star ' in content.lower():
            print(content)
            print("yes harry is presrnt on linr{i}")
            print(i)
        i=i+1

##################################
#make copy of txt file

with open("newline.txt") as f:
    content=f.read()
with open("copy.txt" ,'w') as f:
    f.write(content)


#####################################
file1='copy.txt'    
file2='poem.txt'

with open(file1) as f:
    f1=f.read()
with open(file2) as f:
    f2=f.read()
if f1==f2:
    print("files are identical")
else:
    ("Files are not identical")   
##################################
filename='poem.txt'    
with open(filename,'w') as f:
    f.write('')
#####################
# #################
oldname='poem.txt'
newname='renamed_by_python.txt'    
with open (oldname) as f:
    content=f.read()
with open(newname,'w') as f:
    f.write(content)

