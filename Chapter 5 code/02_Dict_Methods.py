#  now we studied methods of dictionary
info={
    "Name":"Om",
    "Roll No":66,
    "Branch":"Mechatronics"
}

# items() give data of dict in list in the form of tuple
print(info.items())

# keys() returns list of keys 
print(info.keys())

# values() returs value from list
print(info.values())

# update() make update the dict
info.update({"Name":"Saish","Address":"Kopargaon"})
print(info)

# get() method returs value from dict with respected key
print(info.get("Name"))
print(info["Name"])
# so what is diff between them
# if we make it worng input 
print(info.get("New Name")) # it give none 
# print(info["New Name"]) #it give an error

a=info.pop("Name",) # It removes key-value pair and returns their value
print(a)
print(info)
info.popitem() # it removes key value pair in LIFO type Last In First Out
print(info) 