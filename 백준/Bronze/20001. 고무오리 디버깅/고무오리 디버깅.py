p = 0
while 1:
  S = input()
  if '끝' in S: break
  if S=='문제': p += 1
  elif S=='고무오리' and p!=0: p -= 1
  elif S=='고무오리' and p==0: p += 2

if p==0: print('고무오리야 사랑해')
else: print('힝구')