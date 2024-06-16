N, Q = map(int, input().split())
m = [1]
for i in range(1, N+1):
  T = int(input())
  m += [i]*T
for _ in range(Q):
  S = int(input())
  print(m[S+1])