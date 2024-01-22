import sys

h, m, s = map(int, sys.stdin.readline().split())
for _ in range(int(sys.stdin.readline())):
  lst = list(map(int, sys.stdin.readline().split()))
  if len(lst)==2:
    t = h*3600+m*60+s
    t += (lst[1] if lst[0]==1 else -lst[1])
    if t<0:
      t += 86400 #24*3600
    t = t%86400
    h, m, s = t//3600, (t%3600)//60, t%60
  else:
    print(h, m, s)