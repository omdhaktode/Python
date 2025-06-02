# used the functions of string 
#  len() func used to find length of string 
name="om dhaktode"
print(len(name))

# endswith() give is it with same parameter then give true or false
print(name.endswith("todee"))

# startswith() give is it start with same parameter or not 
print(name.startswith("Om"))

#capatalize() used make start char captial 
print(name.capitalize())

#count() used to count how many times char occcur in string
print(name.count("o"))
print(name.count("d"))

#find() used to find word in strng and return start index of word
print(name.find("tode"))
print(name.find('om'))

#replace used to replace the old word to new word
print(name.replace('om','Saish'))
print(name.replace('dhaktode','Jadhav'))