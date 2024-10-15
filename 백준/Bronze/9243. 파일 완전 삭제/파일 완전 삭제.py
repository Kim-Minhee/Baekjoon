# 입력
N = int(input())
F1, F2 = input(), input()

# 풀이
chk = False
if N%2==0:
  if F1==F2:
    chk = True
else:
  f1 = ''
  for f in F1:
    if f=='0':
      f1 += '1'
    else:
      f1 += '0'
  if f1==F2:
    chk = True

# 출력
if chk:
  print('Deletion succeeded')
else:
  print('Deletion failed')