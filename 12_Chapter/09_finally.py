# finally block is used for to execute the block if anything happen it can do its work. 

# let's go i tell you the differece 

try:
    a=int(input("Enter a no: "))
    print(a)

except Exception:
    print('Enter valid value')

print("Thank you for accessing my code")

try:
    a=int(input("Enter a no: "))
    print(a)

except Exception:
    print('Enter valid value')
finally:
    print("Thank you for accessing my code")

# it mainly used in functions if we declare some function and i return a value in it so remaining code can't excuted but finally block is present then it overrite return and excuted.

def main():
    try:
        a=int(input("Enter a no: "))
        print(a)
        return
    except Exception:
        print('Enter valid value')
        return
    finally:
        print("Thank you for accessing my code")
main()