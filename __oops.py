class Employee:
    increment=1.5
    no_of_employees=0
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        Employee.no_of_employees+=1
    def increase(self):
        self.salary=int(self.salary*self.increment)    
print(Employee.no_of_employees)    
harry=Employee('harry','jackson',44000)
print(Employee.no_of_employees)
rohan=Employee('rohan','das',44000) 
print(Employee.no_of_employees)   
