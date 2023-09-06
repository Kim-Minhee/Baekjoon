k, l = map(int, input().split())
chk = True
for r in range(2, l):
  if k%r==0:
    print('BAD', r)
    chk = False
    break
if chk:
  print('GOOD')