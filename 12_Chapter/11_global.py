# using of global keyword we change the scope of variable
a=20
def func():
    a=22      # so this is local variable which now only for function
    print(a)

func()
print(a)

# ----------------------------------

a=20
def func():
    global a
    a=22      # so this is local variable which now only for function
    print(a)

func()
print(a)