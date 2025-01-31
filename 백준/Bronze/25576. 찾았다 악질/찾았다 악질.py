N, M = map(int, input().split())
L = list(map(int, input().split()))

cnt = 0
for _ in range(N-1):
  K = list(map(int, input().split()))

  s = 0
  for i in range(M):
    s += abs(L[i]-K[i])
  if s>2000:
    cnt += 1

if cnt>=(N-1)/2:
  print('YES')
else:
  print('NO')