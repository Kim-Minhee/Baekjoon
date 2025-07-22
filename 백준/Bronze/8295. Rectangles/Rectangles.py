N, M, P = map(int, input().split())

cnt = 0
for i in range(1, N+1):
  for j in range(1, M+1):
    if 2*(i+j)<P:
      continue
    cnt += (N-i+1)*(M-j+1)

print(cnt)