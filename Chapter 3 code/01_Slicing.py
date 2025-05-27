# Define String 
name="Om Dhaktode"
name='Om Dhaktode'
name='''Om Dhaktode'''

# Slice the string 
# Syntax= String variable[Start Index:End Index] do not take EI element 
a=name[3:7]
print(a)

c=name[4] #for a character
print(c)  

# Using negative slicing
print(name[-5:-1])

print(name[:5]) #SI=0
print(name[1:]) #EI=length

# Skil the part
a='abcdefghijklmnopqrstuvwxyz'
print(a[0:26:5])