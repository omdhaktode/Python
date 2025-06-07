# walrus operator (:=)

# simple  program

# n=[1,2,3,4]
# a=len(n)
# if(len(n)>3):
#     print(f"Length of list is {a} and its greater than 3")
# else:
#     pass

# using walrus operator
a=[1,2,3,4]
if (a:=(len(a))) > 3:
     print(f"Length of list is {a} and its greater than 3")















