p, k = map(int, input().split())
chk = True
for r in range(2, k):
  if p%r==0:
    print('BAD', r)
    chk = False
    break
if chk:
  print('GOOD')