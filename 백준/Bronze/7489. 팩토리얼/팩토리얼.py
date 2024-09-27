import math

for _ in range(int(input())):
  N = int(input())
  nf = math.factorial(N)
  for n in str(nf)[::-1]:
    if n!='0':
      print(n)
      break