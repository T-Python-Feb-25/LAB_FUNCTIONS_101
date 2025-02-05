#function 
def pattern (x : int):
    #FOR loop for range
    for i in range(x, 0, -1): #to start from n, to 1 
        for y in range (i, 0, -1): #another FOR to print numbers from i to 1
            print(y, end=" ") #print
        print() #to make line after each lines

#select number
pattern(5)