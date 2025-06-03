# super keyword is used to call constructor from parent class 

class Akash():
    def __init__(self):
       print("My name is Akash")
        
class Vicky(Akash):
    def __init__(self):
        super().__init__()
        print("My name is Vicky")

class Om(Vicky):
    def __init__(self):
        super().__init__()  # call the parent class constructor which is from vicky class
        print("My name is Om")

# o=Akash()
# o=Vicky()
o=Om()
        
