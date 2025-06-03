# create 2D vector and use it in 3D vector

class Vector2D():
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"The 2D Vector is {self.i}i + {self.j}j")

class Vector3D(Vector2D):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f"The 3D Vector is {self.i}i + {self.j}j + {self.k}k")


a=Vector2D(4,5)
a.show()

a=Vector3D(4,2,9)
a.show()