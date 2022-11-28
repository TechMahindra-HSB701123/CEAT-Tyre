marks=[45,78,86,77]
percentage1=(sum(marks)/400)*100
marks1=[78,88,91,88,777]
per=(sum(marks1)/5)*100
print(percentage1,per)



math=int(input("Enter math marks:"))
eng=int(input("Enter eng marks:"))
science=int(input("Enter science marks:"))
history=int(input("Enter history marks:"))
total=[math,eng,science,history]
percentage=(sum(total)/400*100)
print('you have scored{} in math {} in english {} in science {} in history'.format(math,eng,science,history),"and",percentage,"percentage")