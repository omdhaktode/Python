# a file contain "Python" word so write the program to replace them "Java"

with open("Python.txt") as f:
    data=f.read()
    
newdata=data.replace("Python","Java")

with open("Python.txt","w") as f:
    f.write(newdata)

