# code for to check two file contents are same or not
# in that we used words.txt and copy.txt who have same data returns true

def check():
    with open("words.txt") as f:
        content=f.read()

    with open("copy.txt") as f:
        copy_content=f.read()

    if(content==copy_content):
        return True
    else:
        return False
    
print(check())