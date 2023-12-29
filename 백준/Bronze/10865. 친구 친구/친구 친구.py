import sys

n, m = map(int, sys.stdin.readline().strip().split())
l = [0]*n
for _ in range(m):
  a, b = map(int, sys.stdin.readline().strip().split())
  l[a-1] += 1
  l[b-1] += 1
for i in l:
  print(i)