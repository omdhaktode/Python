# convert celsius to fahrenheit

def conv(f):
    result=5*(f-32)/9
    return result


far=int(input("Enter temperature in fahrenheit: "))
result=conv(far)
print(f"Temperature in celsius is {round(result,2)}") # in that we used round func to round the value