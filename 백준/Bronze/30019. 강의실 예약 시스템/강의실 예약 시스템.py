import sys

N, M = map(int, sys.stdin.readline().split())

n = [True]*(N+1)
for _ in range(M):
  K, S, E = map(int, sys.stdin.readline().split())
  if n[K]==True:
    n[K] = E
    print('YES')
  elif n[K]<=S:
    n[K] = E
    print('YES')
  else:
    print('NO')