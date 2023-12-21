m = r = c = 0
for i in range(9):
  l = list(map(int, input().split()))
  if max(l)>=m:
    m = max(l)
    r = i+1
    c = l.index(m)+1
print(m)
print(r, c)