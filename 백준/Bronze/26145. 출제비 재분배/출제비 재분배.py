N, M = map(int, input().split())
S = list(map(int, input().split()))
r = S + [0]*M
for i in range(N):
  T = list(map(int, input().split()))
  for j, t in enumerate(T):
    r[i] -= t
    r[j] += t
print(*r)