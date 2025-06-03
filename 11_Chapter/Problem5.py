# calculate vector and overload + and * operator also implement the length function

class Vector():
    def __init__(self,l):# a,b,c
        # self.a=a
        # self.b=b
        # self.c=c
        self.l=l

    # def __add__(self,other):
    #     result= Vector(self.a+other.a,self.b+other.b,self.c+other.c)
    #     return result
    # def __mul__(self,other):
    #      result= self.a*other.a+self.b*other.b+self.c*other.c
    #      return result
    
    # def __str__(self):
    #     return f"{self.a}i + {self.b} j + {self.c}k"
    
    def __len__(self):
        return len(self.l)
    
# v1=Vector(2,3,4)
# v2=Vector(5,6,7)
# v3=Vector(8,9,1)
v4=Vector([8,9,1])
print(len(v4))

# print(v1+v2)
# print(v1*v2)

# print(v1+v3)
# print(v1*v3)