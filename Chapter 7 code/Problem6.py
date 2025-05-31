# calculate factorial of no 

no=int(input('Enter a no: '))
fact=1
for i in range(1,no+1):
    fact*=i
print(f'Factorial of {no} is {fact}')