s, e, a, f = 0, 0, 0, 0
for _ in range(int(input())):
  G, C, N = map(int, input().split())
  if G==1:
    f += 1
  elif C==1 or C==2:
    s += 1
  elif C==3:
    e += 1
  elif C==4:
    a += 1
print(s)
print(e)
print(a)
print(f)