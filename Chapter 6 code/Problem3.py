# check elements present in message 

p1="are"
p2="of"
p3="is"
p4="was"

user=input('Enter a message:')

if((p1 in user) or (p2 in user) or (p3 in user) or (p4 in user)):
    print("This is not a valid message")
else:
    print("Messge is sent...")