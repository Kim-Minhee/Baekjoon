n, t = map(int, input().split())
tt = list(map(int, input().split()))
h, c = 0, 0
for t_ in tt:
  h += t_
  if h>t:
    break
  else:
    c += 1
print(c)