# now we have to replace words by # * len(word)
words=["om","sai","samadhan"]

with open("words.txt",'r') as f:
    content=f.read()

for word in words:
    content=content.replace(word,"#"*len(word))

with open("words.txt","w") as f:
    f.write(content)
