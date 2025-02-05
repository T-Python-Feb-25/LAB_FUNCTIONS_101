def print_decreasing_numbers(start:int):
    ''' Prints a pattern where each row starts from 'start' and decreases by 1 until 1. Each new row starts one number lower, until the last row with just 1.
    Parameters:
    start(int): The starting number for the pattern.
    '''
    output=""
    while start>0:
        for current_number in range(start,0,-1):
           output+=str(current_number) +" "
        start-=1
        output+="\n"
    print(output)


print_decreasing_numbers(5)
print(print_decreasing_numbers.__doc__)
