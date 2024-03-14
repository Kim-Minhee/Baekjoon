def f(x):
  return str(x)[-1]

N, K = map(int, input().split())
r = list()
for x in range(1, N+1):
  if f(x)!=f(K) and f(x)!=f(2*K):
    r.append(x)
print(len(r))
print(*r)