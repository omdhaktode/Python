# @classmethod decorator is used to bound to the class not to the object of the class

class Akash():
    a=10
    @classmethod
    def show(cls):
        print(f"Value of a is {cls.a}")

o=Akash()
o.a=33
o.show()


# first code give output as a=33 after classmethod shows a=10