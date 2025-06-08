# find the maximum from list and using reduce  
from functools import reduce  

list=[333,2,1,1111,33]
def max(a,b):
    if(a>b):
        return a
    return b

result=reduce(max,list)
print(result)
    



