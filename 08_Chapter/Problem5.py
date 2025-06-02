# convert distance in inches to cm 

def conv(inches):
    return inches*2.54

cm=int(input("Enter distance in cm: "))
result=conv(cm)
print(f"Distance in {cm}cm to inches is {round(result,1)}")