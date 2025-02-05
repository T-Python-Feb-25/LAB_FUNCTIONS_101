def number(n:int) -> str:
  result = " "
  for i in range(n, 0, -1):
      for j in range(i, 0, -1):
        result += str(j) + " "
      result += "\n"
  return result
n= 5
pattern = number(n)
print(pattern )
