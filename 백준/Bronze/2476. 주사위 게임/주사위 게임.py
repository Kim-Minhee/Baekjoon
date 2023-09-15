n, m = int(input()), 0
for _ in range(n):
  a, b, c = map(int, input().split())
  dice, p = {a, b, c}, 0
  if len(dice)==1:
    p = a*1000+10000
  elif len(dice)==3:
    p = max(a, b, c)*100
  else:
    d = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    d[a] += 1
    d[b] += 1
    d[c] += 1
    for i, v in d.items():
      if v==2:
        p = i*100+1000
        break
  if p>m:
    m = p
print(m)