import sys

N, S = sys.stdin.readline().split()

r = 0
for _ in range(int(N)):
  I, C = sys.stdin.readline().split()
  if S in I.split('_'):
    r += int(C)

print(r)