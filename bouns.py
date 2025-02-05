def result(num:int):
    ''' This function takes a number and then prints in each row the numbers preceding the number sequentially. '''
    saver = ""
    for line in range(num):
        for i in range(num - line,0,-1):
            saver += "{}".format(i)
        saver += "\n"
    return saver

number_result = result(6)
print(type(number_result))
print(number_result)
print(result.__doc__)