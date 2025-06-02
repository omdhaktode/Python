# find student is passed or failed if we enter marks of 3 subject and total of marks is greter than 40% and in each
# subject mark is greater than 33%

sub1=int(input('Enter subject1 mark:'))
sub2=int(input('Enter subject2 mark:'))
sub3=int(input('Enter subject3 mark:'))

total=(sub1+sub2+sub3)/3

if(sub1>30 and sub2>30 and sub3>30 and total>40):
    print("You are passed:",total)
else:
    print("You are failed:",total)