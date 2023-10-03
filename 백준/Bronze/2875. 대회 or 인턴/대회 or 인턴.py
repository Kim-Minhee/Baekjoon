n, m, k = map(int, input().split())
t = 0
while True:
  if (n-2)>=0 and (m-1)>=0 and (n+m-3)>=k:
    n -= 2
    m -= 1
    t += 1
  else:
    break
print(t)