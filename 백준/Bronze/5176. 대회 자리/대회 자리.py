for _ in range(int(input())):
  P, M = map(int, input().split())
  m = [1]*(M+1)
  cnt = 0
  for _ in range(P):
    n = int(input())
    if m[n]:
      m[n] = 0
    else:
      cnt += 1
  print(cnt)