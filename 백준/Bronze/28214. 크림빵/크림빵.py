N, K, P = map(int, input().split())
C = list(map(int, input().split()))
cnt = 0
for i in range(0, N*K, K):
  c = 0
  for j in range(K):
    if C[i+j]==1:
      c += 1
  if c>(K-P):
    cnt += 1
print(cnt)