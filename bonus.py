def generate_decreasing_number_pattern(start:int)->str:
    ''' Prints a pattern where each row starts from 'start' and decreases by 1 until 1. Each new row starts one number lower, until the last row with just 1.
    Parameters:
    start(int): The starting number for the pattern.
    return:
    str: The generated pattern as a string.

    '''
    output=""
    while start>0:
        for current_number in range(start,0,-1):
           output+=str(current_number) +" "
        start-=1
        output+="\n"
    return output


result=generate_decreasing_number_pattern(5)
print(result)
print(generate_decreasing_number_pattern.__doc__)
