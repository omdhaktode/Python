# in problem 2 add static method to greet user


import math

class Calculator:
    
    def __init__(self,no):
        self.no=no
    
    def square(self):
        print(f"Square of {self.no}= {self.no**2}")
    def square_root(self):
        print(f"Square root of {self.no}= {math.sqrt(self.no)}")
    def cube(self):
        print(f"Cube of {self.no}= {self.no**3}")
        
    @staticmethod
    def greet():
        print("Hello user, now you are accesing functionality to find sqaure,cube and square root of no")


o1=Calculator(16)
o1.greet()
o1.square()
o1.square_root()
o1.cube()



