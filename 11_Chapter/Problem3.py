# make a class of employeed where we find salary after increment and increment

class Employye():
    salary=200
   
    
    @property
    def salaryafterincrement(self):
        return (self.salary+self.salary * (self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment=((salary/self.salary)-1)*100
         

e=Employye()
e.salaryafterincrement=250
print(e.increment)