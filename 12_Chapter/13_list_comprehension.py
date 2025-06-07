# in that we solve list comprehension

list=[1,2,3,4,5]

square_list=[]

for i in list:
    square_list.append(i**2)

print(square_list)

# above code we can write in single line

list=[1,2,3,4,5]

square_list=[i**2 for i in list]

print(square_list)