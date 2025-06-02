# remove element from list and also strip if word is present in it


def remove(l,word):
    empty=[]
    for item in l:
        if (l!=word):
            empty.append(item.strip(word))
    return empty

l=['Akash',"Rohan","an"]
print(remove(l,"an"))