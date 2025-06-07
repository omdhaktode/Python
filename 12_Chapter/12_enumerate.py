# so why we used enumerate 

list=[2,4,6,8,10]
index=0
for item in list:
    print(f"The no at index {index} is {item}")
    index+=1


# enumerate is used to give index as well as item

list=[1,2,3,4,5]
for index,item in enumerate(list):
    print(f"The no at index {index} is {item}")
