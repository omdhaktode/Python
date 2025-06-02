# we used write mode for files and write some content in it.

str="Wait for some time, soon i do comeback..!" # write some string

file=open("new.txt","w") # open new file in write mode
 
file.write(str) # used write() to add str in file

file.close() #finally close the file

