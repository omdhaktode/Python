# use filter and give no's which is divisible by 5

def show(n):
    if(n%5==0):
        return True
    return False

l =[4*i for i in range(1,11)]

result=filter(show,l)

print(list(result))