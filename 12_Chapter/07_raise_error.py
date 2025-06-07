# we raise the error using raise 

# purpose: we know try-catch use for to not crash the code but developer should know it make critical error so our code will be crashed

a=int(input("Enter no a: "))
b=int(input("Enter no b: "))

if(b==0):
    raise ZeroDivisionError("You can't enter 0 as value of b")
else:
    c=a/b
    print(f"The division is {c}")
