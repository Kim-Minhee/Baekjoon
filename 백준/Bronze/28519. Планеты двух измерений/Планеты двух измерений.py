n, m = map(int, input().split())
if abs(m-n)>1:
  print(2*min(n, m)+1)
else:
  print(n+m)