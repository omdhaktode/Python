# print a table in reverse order using for loop

no=int(input("Enter No: "))
# for i in range(10,0,-1):
#     print(f"{no} * {i} = {no*i}")

for i in reversed(range(1,11)):
     print(f"{no} * {i} = {no*i}")
