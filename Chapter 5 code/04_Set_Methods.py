# add() method adds elements in sets
a={1,23,3,"Akash","Vishal"}
a.add("Tara")
print(a,type(a))

# len() gives length of set
a={1,2,3,4,5}
print(len(a))

# remove() methods removes elements and update set
a={1,2,3,4,5}
a.remove(3)
print(a)

# pop() romoves any element from set and remove it
a={1,2,3,4,5}
e=a.pop()
print(e)

# clear() ddelete all elements from set
a={1,2,3,4,5}
a.clear()
print(a)

# union() print combine all elments in one and print and which is not allow duplicates
a={1,2,3,4}
b={5,6,7,8}
print(a.union(b))

# intersection() take same elements from both sets and give uniques
a={1,2,3,4}
b={5,6,1,7,8}
print(a.intersection(b))


