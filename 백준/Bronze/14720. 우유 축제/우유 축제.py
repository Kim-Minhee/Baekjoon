n = int(input())
l = list(map(int, input().split()))
m, c = 0, 0
if 0 in l:
  c += 1
  for v in l[l.index(0)+1:]:
    if m!=2 and v==m+1:
      c += 1
      m = v
    elif m==2 and v==0:
      c += 1
      m = v
  print(c)
else:
  print(0)