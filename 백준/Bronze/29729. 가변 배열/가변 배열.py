import sys

S, N, M = map(int, sys.stdin.readline().split())
e = 0
for _ in range(N+M):
  o = int(sys.stdin.readline())
  if o==1:
    e += 1
  else:
    e -= 1
  if e>S:
    S *= 2
print(S)