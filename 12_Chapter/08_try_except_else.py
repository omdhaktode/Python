# we used else with try-catch block and when try is excuted then else excuted either it can't excuted

try:
    a=int(input("Enter a no: "))
    print(a)
except Exception:
    print("You entered invalid value")
else:
    print("Thank you for accessing my code")