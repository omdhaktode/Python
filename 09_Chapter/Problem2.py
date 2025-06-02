# make function game() in that if you get highscore  while playing game then add in highscore.txt 
# and print score 

import random as r

def game():
    print("You are playing game...")
    score=r.randint(1,100)
    print("Your score is: ",score)
    with open("highscore.txt") as f:
        highscore=f.read()
        if(highscore!=""):
            highscore=int(highscore)
        else:
            highscore=0

    if(score>highscore):
        with open("highscore.txt","w") as f:
            f.write(str(score))
    return score

game()