def get_pattern_as_string(n):
    result = ""
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            result += str(j) + " "
        result += "\n"
    return result

pattern = get_pattern_as_string(5)
print(pattern)
