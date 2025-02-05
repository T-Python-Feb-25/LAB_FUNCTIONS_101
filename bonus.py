def generate_pattern(n: int) -> str:
    """
    Generates a pattern of numbers in descending order starting from `n` down to 1.

    This function takes an integer `n` as input and generates a pattern where each line 
    starts from a number `i` (where `i` is from `n` down to 1) and decrements to 1.
    Each subsequent line contains one less number than the previous line.

    Parameters:
    n (int): The number from which to start the pattern. The pattern will decrement 
             line by line until 1.

    Returns:
    str: The pattern as a string with each line separated by a newline character.

    Example:
    If n = 5, the function will return:
    "5 4 3 2 1\n4 3 2 1\n3 2 1\n2 1\n1"
    """
    # Initialize an empty string to hold the pattern
    pattern = ""
    
    # Loop through numbers from n to 1
    for i in range(n, 0, -1):
        # Create the descending part of the pattern
        line = " ".join(str(x) for x in range(i, 0, -1))
        # Add the line to the pattern string, followed by a newline
        pattern += line + "\n"
    
    # Return the generated pattern as a string
    return pattern

# Example usage:
pattern = generate_pattern(5)

# Print the generated pattern
print(pattern)