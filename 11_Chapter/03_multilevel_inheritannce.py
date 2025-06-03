# in that we have multilevel inheritance in that derived class -> child class -> child class senario implemented

class College():
    def college(self):
        print("I am a College")

class Engineering(College):
    def engineering(self):
        print("I am Engineering College")

class Diploma(Engineering):
    def diploma(self):
        print("I am diploma college")

d=Diploma()
d.college()
d.engineering()
d.diploma()