# in that we demonstart elif case

a=int(input('Enter your age:'))

if(a>=18):
    print("Welcome, you are in adult now")

elif(a<0):
    print("You are entering invalid age")

elif(a==0):
    print("You are entering 0 age it is also invalid")

else:
    print("Sorry, you are less than 18")

print("End of program")