# check the python present in which line
lineno=1
with open("log.txt",'r') as f:
    line=f.readlines()

for l in line:
    if("python" in l):
        print("Line no:",lineno)
        break
    
    lineno+=1
else:
    print("Not in file")