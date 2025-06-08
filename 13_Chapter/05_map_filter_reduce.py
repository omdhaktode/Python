from functools import reduce
# The map() function is a built-in Python function that allows you to apply a given function to each item of an iterable (like a list, tuple, etc.) and returns an iterator (a map object) of the results.

l=[1,2,3,4,5]

squarelist=lambda x:x*x

result=map(squarelist,l)

print(list(result))


# The filter() function is used to select elements from an iterable (like a list, tuple, etc.) based on a function that tests each element. It returns an iterator containing all elements for which the function returns True.

l=[1,2,3,4,5]

def even(n):
    if(n%2==0):
        return True
    return False

result=filter(even,l)
print(list(result))

# The reduce() function is used to cumulatively apply a function to items in an iterable, reducing the sequence to a single value. It's part of Python's functional programming toolkit.

product=lambda a,b:a*b

result=reduce(product,l)

print(result)