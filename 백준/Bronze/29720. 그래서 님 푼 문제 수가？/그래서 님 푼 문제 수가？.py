N, M, K = map(int, input().split())
mi, ma = N-M*K, N-M*(K-1)-1
if mi<0:
  mi = 0
print(mi, ma)