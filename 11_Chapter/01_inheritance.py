# basic syntax of inheritance 
# inheritance means child class aquire properties from base class

class College:
    def show(self):
        print("I am College")

class Student(College):
    def say(self):
        print("I am Student")

s=Student()
s.show()
s.say()