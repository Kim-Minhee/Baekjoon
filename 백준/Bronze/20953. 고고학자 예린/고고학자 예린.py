import sys

for _ in range(int(sys.stdin.readline())):
  a, b = map(int, sys.stdin.readline().split())
  r = (a+b-1)*(a+b)//2*(a+b)
  print(r)