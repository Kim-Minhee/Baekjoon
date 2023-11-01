import math

while 1:
  b, n = map(int, input().split())
  if b==n==0:
    break
  a1 = math.ceil(b**(1/n))
  a2 = a1-1
  if abs(b-a1**n)<abs(b-a2**n):
    print(a1)
  else:
    print(a2)