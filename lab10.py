def print_num(n: int):
    
    for i in range(n):  
        for j in range(n - i, 0, -1):
            print(j, end=' ') 
        print()  



num= int(input("Please enter a positive integer: "))


print_num(num)