# 입력
I = list(map(str, input().split('|')))

# 풀이
af, al, cf, cl = 0, 0, 0, 0
for i in I:
  if i[0] in 'ADE':
    af += 1
  elif i[0] in 'CFG':
    cf += 1

if af==cf:
  if I[-1][-1] in 'ADE':
    af += 1
  elif I[-1][-1] in 'CFG':
    cf += 1

# 출력
if cf>af:
  print('C-major')
elif cf<af:
  print('A-minor')