# check log.txt file contain python or not

def check():
    with open("log.txt",'r') as f:
        content=f.read()

    if("python" in content):
        return True
    else:
        return False
        
a=check()
print(a)    