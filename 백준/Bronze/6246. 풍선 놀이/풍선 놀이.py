N, Q = map(int, input().split())
b = [1]*(N+1)
for _ in range(Q):
  L, I = map(int, input().split())
  for i in range(L, N+1, I):
    if b[i]:
      b[i] = 0
print(sum(b)-1)