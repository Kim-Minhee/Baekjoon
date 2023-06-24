a, b = map(int, input().split())
n = int(input())
for _ in range(n):
  e, p = int(input()), int()
  if e<=1000:
    p += a*e
  else:
    p += a*1000
    p += b*(e-1000)
  print(e, p)