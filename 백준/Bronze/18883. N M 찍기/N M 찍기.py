N, M = map(int, input().split())
i = 1
for _ in range(N):
  l = list()
  for _ in range(M):
    l.append(i)
    i += 1
  print(*l)