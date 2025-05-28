#  Tuple is Immutable
a=(1,2,3,4,5)
print(type(a))

#if we want to create empty tuple then
a=()
print(type(a))
# but if we want to create single element tuple
a=(1)
print(type(a)) #so python know this is an int value which is enclosed in bracket

#so we have to add , after elment so python understand it is a tuple
a=(1,)
print(type(a))

#we also made multiple type values in single tuple
a=("Om","Akash",22,33,44,55.55)
print(type(a))
print(a)

# count the value present in the tuple
a=(1,1,1,3,2,5,6)
no=a.count(1)
print(no)

#index() write the index of value of first occurance present in tuple
no=a.index(1)
print(no)
# no=a.index(7) #give value error beacuse element not present in tuple
print(no)
# concatanate the two tuples
a=(1,2,3,4)
b=(4,5,6,7)
print(a+b) 

# want repatative tuple
a=(1,2,3)
print(a*3)

# length of tuple
print(len(a))

# membership operator (in)
print(4 in a)

# min and max from tuple
min=min(a)
max=max(a)
print(min)
print(max)

# slicing the tuple
sli=a[3:]
print(sli)

a=(1,2,3,4,5,6,7,8,9,0)
sli=a[0:8:2]
print(sli)

