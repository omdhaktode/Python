# we have to print content of 3 files if they exist or give not present
try:    
    with open("1.txt",'r') as f:
        print(f.read())
except Exception as e:
    print(e)
try:    
    with open("2.txt",'r') as f:
        print(f.read())
except Exception as e:
    print(e)
try:        
    with open("3.txt",'r') as f:
        print(f.read())
except Exception as e:
    print(e)


print('Thank You...')