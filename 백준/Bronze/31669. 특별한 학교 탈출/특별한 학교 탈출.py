N, M = map(int, input().split())
e = ['O']*M
for _ in range(N):
  OX = input()
  for i, v in enumerate(OX):
    if v=='O':
      e[i] = 'X'
if 'O' in e:
  print(e.index('O')+1)
else:
  print('ESCAPE FAILED')