

def pattern(x):
    for y in range(x, 0, -1):
        for z in range(y, 0, -1):
            print(z, end=" ")
        print()
print(pattern.__doc__)
pattern(5)



def pattern(x):
    
    
    pattern = ""
    for y in range(x, 0, -1):
        for z in range(y, 0, -1):
            pattern += str(z) + " "  # Append numbers with space
        pattern = pattern.rstrip() + "\n"  # Trim trailing space and add newline
    return pattern

# Store the pattern in a variable and print it
pattern_result = pattern(5)
print(pattern_result)
