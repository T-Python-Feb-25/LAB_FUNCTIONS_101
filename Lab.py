def num(x:int):
    
    ''' this function takes 1 parameter of type int , then it prints out the result formatted like the following patter  
3 2 1   
2 1   
1   

'''

    while x!=0:
        z=x
        while z!=0:
            print(z,"", end="")
            z-=1
            
        x-=1
        print()


print(num.__doc__)        
num(7)  

      