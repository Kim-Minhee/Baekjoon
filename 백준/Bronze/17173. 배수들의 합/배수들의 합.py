N, M = map(int, input().split())
K = list(map(int, input().split()))

chk = [0]*(N+1)
for k in K:
  i = 1
  while k*i<=N:
    if chk[k*i]==0: chk[k*i] = 1
    i += 1

r = 0
for n in range(len(chk)):
  if chk[n]==1: r += n

print(r)