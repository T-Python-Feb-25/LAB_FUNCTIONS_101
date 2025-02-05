def number(j:int):
    'this function will print the numbers as a string from 10 to 1 in descending order'
    phrase =''
    for i in range(10,0,-1):
        for n in range(i,0,-1):
            phrase += f'{n}'
        phrase += '\n'
    return phrase
r = number(10)
print(type(r))
print(r)
print(number.__doc__)


