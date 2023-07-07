import math

n = int(input())
for _ in range(n):
  a1, p1 = map(int, input().split())
  r1, p2 = map(int, input().split())
  s = a1*p1
  w = math.pi*(r1**2)
  if s>w:
    print('Slice of pizza')
  else:
    print('Whole pizza')