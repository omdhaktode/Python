# if string is immutable but we can change the data in same list 
friends=[0,1,1.22,True,False,"Om","Saish","Akash",'a']
print(friends[6])
friends[5]="Kartik"
print(friends)

# like string we can done a slicing of list
print(friends[1:6])
print(friends[0:9:2])

