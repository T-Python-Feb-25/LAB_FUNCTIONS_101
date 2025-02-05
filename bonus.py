def pattern(number):
    concate = ""
    '''This Function Return The Given Number in reverse pyramid'''
    for i in range(number):
        for j in range(number - i,0,-1):
            concate += f"{j} "
        concate += "\n"
    return concate
            



result = pattern(8)
print(type(result))
print(result)