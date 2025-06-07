# match case is coming in python 3.10 version it is just like switch case

def choose(option):
    match option:
        case 200:
            print("You are the One")
        case 300:
            print("You are the Second")
        case 400:
            print("You are the third")
        case _:
            print("You are the default")

a=int(input('Enter Option: '))
choose(a)