# check no is prime or not

no=int(input('Enter a No: '))
for i in range(2,no):
    if(no%i==0):
       print(no,"is not prime no")
       break
else:
    print(no,'is prime no') 


no = int(input('Enter a No: '))

if no <= 1:
    print(f'{no} is not prime no')
else:
    is_prime = True
    for i in range(2, int(no**0.5) + 1):  # More efficient range
        if no % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f'{no} is prime no')
    else:
        print(f'{no} is not prime no')