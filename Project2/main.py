# guess a no with system if it's correct then you are win 

import random as r 
pc_no=r.randint(1,100)
a=-1
guess=1
print(pc_no)
while(a!=pc_no):
    a=int(input("Guess the Number: "))
    if(a>pc_no):
        print("Please enter Lower number...")
        guess+=1
    elif(a<pc_no):
        print("Please enter higher number...")
        guess+=1


print(f"You guess the {pc_no} in {guess} attempts.")