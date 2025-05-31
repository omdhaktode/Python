# determine factorial of no using recursion

def recursion(n):
    if(n==0 or n==1):
        return 1
    return n*recursion(n-1)

n=int(input('Enter No: '))
print(recursion(n))