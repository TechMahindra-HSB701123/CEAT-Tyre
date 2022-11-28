




g="         Harry is a dancer            "
print(g)
print(g.strip())







def remove_and_strip(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()
this='     Harry is Good         '
n=remove_and_strip(this,"Harry")
print(n)



