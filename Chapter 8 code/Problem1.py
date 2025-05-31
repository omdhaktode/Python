# find greatest of three numbers

def greater(a,b,c):
    if(a >b and a>c):
        print(f"{a} is greatest")  
    elif(b >a and b>c):
        print(f"{b} is greatest")
    elif(c >a and c>b):
        print(f"{c} is greatest")

a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
greater(a,b,c)