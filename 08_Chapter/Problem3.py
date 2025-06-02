# to calculate value of 1st n natural no's using recursive

def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)

no=int(input("Enter no: "))
print(f"Addition is {sum(no)}")