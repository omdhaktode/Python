# in that we used self because of self refers to the current instance.
# self is convention we can write anything for ex ss,uv 


class Info:
    name="Akash"
    roll_no=22

    def printInfo(self):
        print(f"My name is {self.name} and my roll no is {self.roll_no}.")

    def getInfo(uv):
        print("In 3 sec Program will run..")

    def something_happen(ss):
        print(f"now you are name is {ss.name}.")

om=Info()
om.getInfo()
print("...........1 sec")
print("...........2 sec")
print("...........3 sec")
om.printInfo()
om.name="Rohit" # create instance variable
om.something_happen()