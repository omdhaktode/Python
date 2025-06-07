# store the tables generated in problem3 in tables.txt


no=int(input("Enter a no: "))
list=[no * i for i in range(1,11)]

with open("tables.txt",'a') as f:
    f.write(f"table of {no}: {str(list)} \n")
