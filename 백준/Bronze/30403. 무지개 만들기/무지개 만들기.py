N, S = input(), input()

upper_chk, lower_chk = True, True
for u in 'ROYGBIV':
  if u not in S:
    upper_chk = False
    break
for l in 'roygbiv':
  if l not in S:
    lower_chk = False
    break

if upper_chk and lower_chk: print('YeS')
elif upper_chk: print('YES')
elif lower_chk: print('yes')
else: print('NO!')