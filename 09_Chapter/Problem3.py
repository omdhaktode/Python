# write a code to generate tables from 2 to 20 and add in differnt file for each table

def generator(n):
    empty=""
    for i in range(1,11):
        empty+=f"{n} * {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt","w") as f:
        f.write(empty)
for i in range(2,21):
    generator(i)