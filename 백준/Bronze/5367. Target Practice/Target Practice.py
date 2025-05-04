N = int(input())

line = '|' + '-'*(N-2) + '|'
lines = [line]
for i in range((N-2)//2):
  l = '|'
  l += ' '*i
  l += '*'
  l += ' '*(N-4-2*i)
  l += '*'
  l += ' '*i
  l += '|'
  lines.append(l)

mid = '|' + ' '*((N-3)//2) + '*' + ' '*((N-3)//2) + '|'
lines.append(mid)

for l in lines:
  print(l)
for l in lines[-2::-1]:
  print(l)