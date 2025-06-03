# in that we saw operator overloading it is used for define custom behavior for built-in operators (like +, -, *, ==, etc.)
 

class Addition():
    def __init__(self,n):
        self.n=n

    def __add__(self,m):
        return self.n + m.n
    
    def __mul__(self,f):
        return self.n*f.n
    
a=Addition(5)
b=Addition(5)
print(a+b)
print(a*b)