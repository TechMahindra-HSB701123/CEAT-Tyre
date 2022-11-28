mydict={"Fast":"in aQuick Manner","Harry":"A Coder","Himansu":"A Govt emp","Harry":"A Codetttt",'anotherdict':'python',
'llist':[10,'Love',121]}
print(mydict["Fast"])
print(mydict)
print(mydict['llist'])
print(mydict)
mydict['Harry']='A Teacher'
print(mydict)




#key
n={"Fast":"in aQuick Manner","Harry":"A Coder","Himansu":"A Govt emp","Harry":"A Codetttt",'anotherdict':'python',
'llist':[10,'Love',121]}
print(type(list(n.keys())))
print(list(n.values()))
print(n.keys())
print(n.items())# for all content
updated={"ask":[10,77,99],45:'himansu'}
n.update(updated)
print(n)
print(n.get("Harry"))
print(n.get("Harry2"))



##write aprogramme to creat a dictonary of Hindi words with English Translation
abc={"pankha":"Fan","Khana":"Food","Gaana":"song","anda":"egg"}
print("option are::",abc.keys())
print(abc.get(input("Enter in dictonatry of hindi to english:::")))


