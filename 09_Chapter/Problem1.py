# read poem from file poems.txt and check file contains twinkle or not

# Method 1

f=open("poems.txt")
data=f.read()
print(data)

f.seek(0)
word="Twinkle"
for line in f:
    if word in line:
        print(True)
        break
else:
    print(False)

f.close()

# Method 2

with open("poems.txt") as f:
    data=f.read()
    print(data)

    if("Twinkle" in data):
        print("Twinkle is present")
    else:
        print("Twinkle is not present")