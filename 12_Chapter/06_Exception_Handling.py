# using try-catch block our code can't be crashed 

# let do with normal example

a=int(input('Enter a No: ')) # if we put a wrong value here so our code will be crashed
print(a) 
print('Thank You')


# using try-catch

try:
    a=int(input("Enter a No: "))
    print(a)

except Exception :
    print("Invalid Output, Please enter no value")

print("Thank you guys")


# we can specify the specific error

try:
    a=20
    b=int(input('Enter a No to divide no 20: '))
    c=a/b
    print("Division is ",c)

except ZeroDivisionError:
    print("You entered 0,it cannot divide any no..")

except Exception as e:
    print("Error, Enter valid no...")
