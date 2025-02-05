def print_pattern(n: int):
    """
    Prints a pattern of numbers in descending order starting from `n` down to 1.

    This function takes an integer `n` as input and prints a pattern where each line 
    starts from a number `i` (where `i` is from `n` down to 1) and decrements to 1.
    Each subsequent line contains one less number than the previous line.

    Parameters:
    n (int): The number from which to start the pattern. The pattern will decrement 
             line by line until 1.

    Example:
    If n = 5, the function will print:
    5 4 3 2 1
    4 3 2 1
    3 2 1
    2 1
    1
    """
    
    # Loop through numbers from n to 1
    for i in range(n, 0, -1):
        # Create the descending part of the pattern
        line = " ".join(str(x) for x in range(i, 0, -1))
        # Print the line
        print(line)

# Example usage:
print_pattern(9)
# Print the documentation of the function
print("\nFunction Documentation:")
print(print_pattern.__doc__)