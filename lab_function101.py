def task1(num:int):
    '''This function print a upside down pyramid shape start from the number in the parameter until 1. '''
    while num >= 1:
        for i in range(num,0,-1):
            print(i,end=' ')
        num -=1 
        print()
task1(10)
print(task1.__doc__)
