# so basically we define the function in that and we import in another file and use functionality of this file in another file 
print('You have to no accessbality of this code')


if(__name__=="__main__"):
    def add(a,b):
        return a+b

    print(add(20,40))
print(__name__)
