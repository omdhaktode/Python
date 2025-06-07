# we can open multiple file

# basic

with open("file1.txt") as f1:
    pass
with open("file2.txt") as f2:
    pass

# advanced 

with(
    open("file1.txt") as f1,
    open("file2.txt") as f2
):
    pass