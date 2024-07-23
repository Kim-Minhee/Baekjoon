import math
N = int(input())
i = ''
for _ in range(2*N-1):
  i += input()
i = i.replace('/', '//')
print(eval(i))