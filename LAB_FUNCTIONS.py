def number(j:int):
    'this function will print the numbers from 10 to 1 in descending order'
    for i in range(10,0,-1):
        for n in range(i,0,-1):
            print(n,end=' ')
        print()
number(10)
print(number.__doc__)

