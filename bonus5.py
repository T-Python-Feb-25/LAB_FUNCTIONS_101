#function 
def pattern (x : int):
    result = ""
    #FOR loop for range
    for i in range(x, 0, -1): #to start from n, to 1 
        for y in range (i, 0, -1): #another FOR to print numbers from i to 1
            result += str(y) + " "
        result += "\n"
    return result


#assign the result to a variable
patter_result = pattern(5)

#print the result
print(patter_result)