import math

n = int(input())
l, c = math.ceil(n**(1/2)), math.ceil(n**(1/2))
if l*(c-1)>=n:
  print(l, c-1)
elif l*c >=n:
  print(l, c)
else:
  print(l, c+1)