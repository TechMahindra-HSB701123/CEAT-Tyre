#1.break  2.continue   3.pass
1#break
for i in range(10):
    if i==7:
        print("processing is enough .... please breake ",i)
        break
    print("we need",i)



cart=[10,20,110,600,80,90]    
for i in cart:
    if i>100:
        print('insurance is needed',i)
        break
    print('we need',i)

#continue
for i in range(10):
    if i%2==0: 
        print("not needed",i) 
        continue   
    print('need',i)


number=[10,20,0,5,0,30]
for i in number:
    if i==0:
        print("it's an excuse",i)
        continue
    print('Digits',i)



number=[10,20,0,5,0,30]
for n in number:
    if n==0:
        print("Hye how we can divide with zero...........Pagal hogaya kya")
        continue
    print("100/{}={}".format(n,100/n))








 




