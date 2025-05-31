# we maid a snake,water and gun game

""" 
snake=1 
water=-1
gun=0
 """
import random

computer=random.choice([1,-1,0])
you_choose=input('Enter your choice: ')
your_dict={'snake':1,'water':-1,'gun':0}
computer_dict={1:"snake",-1:"water",0:"gun"}
you=your_dict[you_choose]
print("")
print(f"You choose: {you_choose}")
print(f"Computer choose: {computer_dict[computer]}")

if(computer==you):
    print('Its Draw..!')
else:
    if(computer== -1 and you== 1):
        print("You win..!")
    elif(computer== -1 and you== 0):
        print("Computer win..!")
    elif(computer== 1 and you== 0):
        print("You win..!")
    elif(computer== 1 and you== -1):
        print("Computer win..!")
    elif(computer== 0 and you== 1):
        print("Computer win..!")
    elif(computer== 0 and you== -1):
        print("You win..!")
    else:
        print("Something went wrong")

