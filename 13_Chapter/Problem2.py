# write a code to take input form user name,rollno and marks and print using format() function


name=input('Enter your name: ')
rollno=int(input('Enter your roll no: '))
phoneno=int(input('Enter your phone no: '))

a="My name is {}, my roll no is {} and my phone no is {}".format(name,rollno,phoneno)
print(a)