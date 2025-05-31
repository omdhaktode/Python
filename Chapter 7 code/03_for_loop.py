# print elements from list

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
for item in list:
    print(item)

# enumerate() gives both index and value
for index,value in enumerate(list):
    print(f"Index {index}:{value}")

# we take range(start:stop:ste_size) like slice
for i in range(0,len(list),3):
    print(list[i],end=" ")

# print all elements from tuple
a=(1,2,3,4,5,6,7,8)   
for i in a:
    print(i,end=" ")

# use on string
str="omdhaktode"
for i in str:
    print(i,end=" ")

# use for loop with else
a=[1,2,3,4,5,6,7,8]   
for item in a:
    print(item)
else:
    print("Done")

