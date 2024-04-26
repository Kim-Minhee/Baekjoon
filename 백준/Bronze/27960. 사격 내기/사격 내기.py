def cal(s):
  i, l = 10, list()
  while i>=0:
    if 2**i<=s:
      l.append(i)
      s -= 2**i
    i -= 1
  return l

Sa, Sb = map(int, input().split())
la, lb = cal(Sa), cal(Sb)

c = 0
for i in range(10):
  if (i in la and i not in lb) or (i not in la and i in lb):
    c += 2**i
print(c)