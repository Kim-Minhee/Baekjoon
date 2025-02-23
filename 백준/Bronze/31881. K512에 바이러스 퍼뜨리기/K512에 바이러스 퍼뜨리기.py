import sys

N, Q = map(int, sys.stdin.readline().rstrip().split())

computers = [0]*(N+1)
r = N
for _ in range(Q):
  query = list(map(int, sys.stdin.readline().rstrip().split()))
  if query[0]==1:
    if not computers[query[1]]:
      computers[query[1]] = 1
      r -= 1
  elif query[0]==2:
    if computers[query[1]]:
      computers[query[1]] = 0
      r += 1
  else:
    print(r)