# built a class named 'Calculator' calculates no's square,cube and square root
import math

class Calculator:
    def __init__(self,no):
        self.no=no
        print(f"Square of {no}= {no**2}")
        print(f"Cube of {no}= {no**3}")
        print(f"Square root of {no}= {math.sqrt(no)}")


no1=int(input("Enter a no: "))
o1=Calculator(no1)
no2=int(input("Enter a no: "))
o2=Calculator(no2)
no3=int(input("Enter a no: "))
o3=Calculator(no3)
no4=int(input("Enter a no: "))
o4=Calculator(no4)

