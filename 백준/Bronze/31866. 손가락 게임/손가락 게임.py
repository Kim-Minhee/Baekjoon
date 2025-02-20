rsp = {0: '바위', 1: '무효', 2: '가위', 3: '무효', 4: '무효', 5: '보'}

J, I = map(int, input().split())
j, i = rsp[J], rsp[I]

if j==i:
  print('=')
elif i=='무효' or (j=='바위' and i=='가위') or (j=='가위' and i=='보') or (j=='보' and i=='바위'):
  print('>')
else:
  print('<')