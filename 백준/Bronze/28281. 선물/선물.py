n, x = map(int, input().split())
a = list(map(int, input().split()))
m = 2001
for i in range(n-1):
  if a[i]+a[i+1]<m:
    m = a[i]+a[i+1]
print(m*x)