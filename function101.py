def descending (x: int) :
    ''' The function generates a descending pattern of numbers,
where each line starts from a number and decrements
 down to 1, and prints the entire pattern '''
    while x > 0 :
        for i in range(x, 0, -1):
            print(i, end=" ")
        x -=1
        print(" ")


# the bonus question
def desce(x: int) :
    ''' The function generates a descending pattern of numbers,
   where each line starts from a number and decrements
    down to 1, and returns the entire pattern as string'''

    result=""
    while x > 0 :
        for i in range(x, 0, -1):
            result += str(i) + " "
        x -=1
        result += "\n"
    return result


descending(4)

bonus=desce(5)
print(bonus)

