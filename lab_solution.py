
# LAB_FUNCTIONS_101

def pattern_1_function(number:int):
    '''   
    This function Prints a descending pattern of numbers based on a given integer.
    It takes a positive integer that determines the size of the pattern.
    '''
    print(f"the pattern for number {number}")
    for col in range(number,0,-1):
        for row in range(col,0,-1):
            print(row,end=' ')
        print("")
    
pattern_1_function(5)

print(pattern_1_function.__doc__)


def pattern_2_function(number:int)->str:
    '''   
    This function Prints a descending pattern of numbers based on a given integer.
    It takes a positive integer that determines the size of the pattern.
    return the full pattern as string 
    '''
    pattern:str=""

    for col in range(number,0,-1):
        for row in range(col,0,-1):
            pattern+=str(row)+" "
        pattern+="\n"

    return pattern

num_pattern=pattern_2_function(5)
print(num_pattern)

        
    

        
    
