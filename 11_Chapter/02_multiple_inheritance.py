# in that i implement multiple inheritance who contain multiple base class and 1 child class

class Father():
    father_name="default father"

    def father(self):
        print(f"I am your father and my name is {self.father_name}")

class Mother():
    mother_name="default mother"

    def mother(self):
        print(f"I am your mother and my name is {self.mother_name}")

class Son(Father,Mother):
    name="default son"
    
    def son(self):
        print(f"I am your son and my name is {self.name}")

akash=Son()
akash.father()
akash.mother()
akash.son()