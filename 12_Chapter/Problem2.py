# print third,fifth and seven no from list 

list=[1,2,3,4,5,6,7]

for  index,item in enumerate(list):
    if index==2 or index==4 or index==6:
        print(f"The no at index {index} is {item}")