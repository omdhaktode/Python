# create a class Animals -> Pets -> Dog and add bark method in Dog

class Animals():
    pass

class Pets(Animals):
    pass

class Dog(Pets):

    @staticmethod
    def bark():
        print('Bow Bow Bow.....')

a=Dog()
a.bark()