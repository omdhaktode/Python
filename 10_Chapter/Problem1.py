# code of creating class of programmer and in that contain information the programmer who is working in google

class Programmer:
    company="Google"

    def __init__(self,id,name,salary):
        self.id=id
        self.name=name 
        self.salary=salary

prg1=Programmer("111","Om Dhaktode",1200000)
print(prg1.id,prg1.name,prg1.salary)
prg2=Programmer("222","Vikrant Shelhke",2000000)
print(prg2.id,prg2.name,prg2.salary)
        