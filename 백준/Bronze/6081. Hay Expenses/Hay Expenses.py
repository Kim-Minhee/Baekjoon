N, Q = map(int, input().split())

h = [0]
for _ in range(N):
  h.append(int(input()))

for _ in range(Q):
  S, E = map(int, input().split())
  print(sum(h[S:E+1]))