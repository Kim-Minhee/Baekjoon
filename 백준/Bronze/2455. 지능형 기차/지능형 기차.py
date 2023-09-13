t, m = 0, 0
for _ in range(4):
  o, i = map(int, input().split())
  t += i
  t -= o
  if t>m:
    m = t
print(m)