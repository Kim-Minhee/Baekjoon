n, m = int(input()), int(input())
chk, r = False, m
for _ in range(n):
  i, o = map(int, input().split())
  m += i
  m -= o
  if m<0:
    chk = True
  if m>r:
    r = m
if chk:
  print(0)
else:
  print(r)