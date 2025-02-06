def num(x:int):
    
    ''' this function it returns the pattern as a string, then assign the result to a variables and print it. 

'''

    while x!=0:
        z=x
        while z!=0:
            result=str(z)
            print(result,"",end="")
            z-=1
            
        x-=1
        print()
        
print(num.__doc__)        
num(5)  