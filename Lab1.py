def pattern(number:int):
    '''This Function Prints The Given Number in reverse pyramid'''
    for i in range(number):
        for j in range(number - i,0,-1):
            print(j,end=" ")
        print("")


pattern(10)
print(pattern.__doc__)

