def fun(n, k, p):
  return k*n+p*n**2

n, k, p = map(int, input().split())
w = 0
for i in range(1, n+1):
  w += fun(i, k, p)
print(w)