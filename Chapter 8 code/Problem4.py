""" print following pattern using recursion

***
**
*
 """


def pattern(n):
    if(n==1):
        print("*")
        return
    print("*"*n,end=" ")
    print("")
    pattern(n-1)

lines=int(input("Enter no of lines: "))
pattern(lines)