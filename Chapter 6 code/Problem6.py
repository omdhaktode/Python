# display catogary of student marks

marks=int(input("Enter marsks: "))

if(marks>90 and marks<=100):
    print("Ex")
elif(marks>80 and marks<=90):
    print("A")
elif(marks>70 and marks<=80):
    print("B")
elif(marks>60 and marks<=70):
    print("C")
elif(marks>50 and marks<=60):
    print("D")
else:
    print("F")