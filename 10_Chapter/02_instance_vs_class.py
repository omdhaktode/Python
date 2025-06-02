# instance attribute always take preferences over class attributes 

class Student:
    name="om"
    age=21

s1=Student()
s1.name="Akash" # it also known as instance attribute or object attribute 
print(s1.name,s1.age)