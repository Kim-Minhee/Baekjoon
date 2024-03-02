n, t = map(int, input().split())
chk, a = True, 1
for _ in range(t-1):
  if chk:
    a += 1
  else:
    a -= 1
  if a==2*n:
    chk = False
  elif a==1:
    chk = True
print(a)