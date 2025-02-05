n = int(input("enter the number for the loop "))
pattern = ""
i = n
while i > 0:
    j = i
    while j > 0:
        pattern += str(j) + ' '  
        j -= 1  
    pattern += '\n'  
    i -= 1  
print(pattern)

