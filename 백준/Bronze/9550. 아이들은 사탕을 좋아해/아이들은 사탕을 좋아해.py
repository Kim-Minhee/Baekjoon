t = int(input())
for _ in range(t):
  n, k = map(int, input().split())
  cnt = 0
  c = list(map(int, input().split()))
  for i in c:
    cnt += i//k
  print(cnt)