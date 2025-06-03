# in that we implement @property and @value.setter decorator it enables encapsulation and data hiding 

class Student:

    
    @property
    def name(self):
        print(f"My name is {self.fname} {self.lname}")

    @name.setter
    def name(self,values):
        self.fname=values.split(" ")[0]
        self.lname=values.split(" ")[1]
  

s=Student()
s.name="Ritik Roshan"
print(s.fname,s.lname)