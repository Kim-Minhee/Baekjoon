s1, s2 = map(int, input().split())
chk1, chk2 = True, True
for _ in range(s1):
  sa, ma = map(int, input().split())
  if sa!=ma:
    chk1 = False
for _ in range(s2):
  sa, ma = map(int, input().split())
  if sa!=ma:
    chk2 = False

if chk1 and chk2:
  print('Accepted')
elif not chk1:
  print('Wrong Answer')
elif chk1 and not chk2:
  print('Why Wrong!!!')