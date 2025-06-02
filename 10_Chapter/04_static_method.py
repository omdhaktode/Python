""" 
In Python, the @staticmethod decorator is used to define a static method inside a class. Unlike regular instance methods, a static method does not take self or cls (class) as its first parameter.

When to Use @staticmethod?
When the method does not depend on instance or class variables (logic is self-contained).

For utility/helper functions that are related to the class but don't need access to instance data.

When you want to group a function under a class for better code organization.  """


class Info:
    name="Akash"
    roll_no=22

    def printInfo(self):
        print(f"My name is {self.name} and my roll no is {self.roll_no}.")
    @staticmethod
    def getInfo():
        print("In 3 sec Program will run..")
    
    def something_happen(ss):
        print(f"now you are name is {ss.name}.")

om=Info()
om.getInfo()      # call with instance name 
Info.getInfo()    # call with class name 
print("...........1 sec")
print("...........2 sec")
print("...........3 sec")
om.printInfo()
om.name="Rohit" # create instance variable
om.something_happen()
