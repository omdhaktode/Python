# only greet those persons whos names start with s

list=["Akash","Saish","Vaishnavi","Siddhi","Samadhan"]

for item in list:
    if(item.startswith("S")):
        print(f"Welcome {item}, nice to meet you ")
