# find greatest of 4 no's

a1=int(input("Enter no 1:"))
a2=int(input("Enter no 2:"))
a3=int(input("Enter no 3:"))
a4=int(input("Enter no 4:"))

if(a1 >a2 and a1>a3 and a1>a4):
    print(a1," is greater")
elif(a2 >a1 and a2>a4 and a2>a3):
    print(a2," is greater")
elif(a3 >a1 and a3>a2 and a3>a3):
    print(a3," is greater")
elif(a4>a1 and a4>a2 and a4>a3):
    print(a4," is greater")