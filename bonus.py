def pyramidShape(num:int ) ->str:
    '''This function print a upside down pyramid shape start from the number in the parameter until 1. '''
    format = ''
    while num >= 1:
        for i in range(num,0,-1):
            format += str(i) + ' '
        num -=1 
        format += '\n'
    return format
    
result = pyramidShape(5)
print(result)