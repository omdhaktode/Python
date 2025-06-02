file=open("data.txt")
print(file.read())
file.close()

# but i want to do same work and don't want to close file so we used with statement for it.

with open("data.txt") as f:
    print(f.read())