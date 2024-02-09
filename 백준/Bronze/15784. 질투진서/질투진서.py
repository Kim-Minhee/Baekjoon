n, a, b = map(int, input().split())
att = list()
for _ in range(n):
  att.append(list(map(int, input().split())))
j, chk = att[a-1][b-1], True

for i in range(n):
  if (att[a-1][i]>j) or (att[i][b-1]>j):
    chk = False
    break
if chk:
  print('HAPPY')
else:
  print('ANGRY')