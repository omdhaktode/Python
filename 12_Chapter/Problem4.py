# check a/b if zerodivision error found print infinite

try:
    a=int(input('Enter Number 1: '))
    b=int(input('Enter Number 2: '))
    print(a/b)

except ZeroDivisionError as z:
    print(z)

print('Thank You...')