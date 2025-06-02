# check om element present in post

element="Om"

post=input("Enter post: ")

if(element.lower() in post.lower()):
    print("Element is present in post")
else:
    print("Well and good post")