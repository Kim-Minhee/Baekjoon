n, k = map(int, input().split())
y, chk = list(), True
for i in range(1, n+1):
  if n%i==0:
    y.append(i)
  if len(y)==k:
    print(y[k-1])
    chk = False
    break
if chk:
  print(0)