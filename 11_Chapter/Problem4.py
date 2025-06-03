# write a class complex contain complex no's and used overloaded operators with them +,*

class Complex():
    def __init__(self,r,i):
        self.r=r
        self.i=i

    def __add__(self,a):
        return Complex(self.r+a.r,self.i+a.i)
    
    def __mul__(self,b):
        self.real=self.r*b.r-self.i*b.i
        self.img=self.r*b.r+self.i*b.i
        return Complex(self.real,self.img)
    
    def __str__(self):
        return f"{self.r}+{self.i}i"
    
    
c1=Complex(2,1)
c2=Complex(3,2)
print(c1+c2)
print(c1*c2)