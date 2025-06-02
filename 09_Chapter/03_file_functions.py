# in this code we define multiple functions of file functions 

# using readlines() we make list of data

# file=open("data.txt")
# list=file.readlines()
# print(list)
# file.close()

# using readline() print line one by one

# file=open("data.txt")
# line1=file.readline()
# print(line1,type(line1))
# line2=file.readline()
# print(line2,type(line2))
# line3=file.readline()
# print(line3,type(line3))
# line4=file.readline()
# print(line4,type(line4))
# line5=file.readline()
# print(line5,type(line5))
# file.close()

# above code do with help of while loop 

# file=open("data.txt")
# line=file.readline()
# while(line!=""):
#     print(line,type(line))
#     line=file.readline()

# file.close()

# a- append mode used to apend information at the end of file like list 
str="You"
file=open("new.txt",'a')
data=file.write(str+" ")
file.close()













