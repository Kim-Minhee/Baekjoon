g, p, t = map(int, input().split())
t1 = g*p
t2 = g+(t*p)
if t1<t2:
  print(1)
elif t1>t2:
  print(2)
else:
  print(0)