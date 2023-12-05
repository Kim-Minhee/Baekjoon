t = int(input())
for _ in range(t):
  n, d = map(int, input().split())
  cnt = 0
  for _ in range(n):
    v, f, c = map(int, input().split())
    if f>=c*(d/v):
      cnt += 1
  print(cnt)