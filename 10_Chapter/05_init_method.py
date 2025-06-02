# __INIT__ method is constructor in python which is automatically called...

class Student():
    name="Om"
    age=21
    sub="English"
    @staticmethod 
    def tp():
        print("Hello guys, good to see you..")
    
    def __init__(self,name,age,sub): # the methods starting from __ also known for dunder method which is automatically called
        self.name=name 
        self.age=age
        self.sub=sub
        print(f"My name is {self.name} and my age is {self.age} and in my school i choose subject {self.sub}")
       
om=Student("Akash",22,"Science")
om.tp()
print(om.name,om.age,om.sub)