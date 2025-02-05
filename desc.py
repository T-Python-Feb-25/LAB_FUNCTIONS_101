def print_pattern(n: int) -> None:
    
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer greater than zero.")
    
    for i in range(n, 0, -1):
        print(' '.join(str(j) for j in range(i, 0, -1)))

if __name__ == "__main__":
    print(print_pattern.__doc__)
    
    
    try:
        number = int(input("Enter a positive integer: "))
        print_pattern(number)
    except ValueError as e:
        print(f"Error: {e}")