L, C, N = map(int, input().split())

r = []
for _ in range(C):
  S, P = map(int, input().split())
  r.append(abs(N-P)+S)

for i in range(C):
  print(r[i])