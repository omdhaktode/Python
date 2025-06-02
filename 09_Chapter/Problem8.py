# to make a copy of words.txt as copy.txt

with open("words.txt") as f:
    data=f.read()

with open("copy.txt","w") as f:
    f.write(data)
