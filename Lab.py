def result(num:int):
    ''' This function takes a number and then prints in each row the numbers preceding the number sequentially.  '''
    for line in range(num):
        for i in range(num - line,0,-1):
            print(i,end= " ")
        print("")

result(8)
print(result.__doc__)