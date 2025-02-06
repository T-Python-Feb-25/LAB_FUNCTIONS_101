def pattern(n: int):
    for i in range(n, 0, -1):
        line = ' '.join(str(x) for x in range(i, 0, -1))
        print(line)

pattern(10)

print ("\n#################### Bonus ########################\n")
def paternToString(n: int) -> str:
    pattern_lines = []

    for i in range(n, 0, -1):
        line = ' '.join(str(x) for x in range(i, 0, -1))
        pattern_lines.append(line)
    return '\n'.join(pattern_lines)

result = paternToString(10)
print(result)


'''
this is the LAB_CONDITIONALS Bonus 
Feb5, 2025
By Mohammed Albushaier
'''
