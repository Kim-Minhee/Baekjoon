y, l = int(input()), input()
a = b = 0
for i in l:
  if i=='A':
    a += 1
  else:
    b += 1
if a>b:
  print('A')
elif b>a:
  print('B')
else:
  print('Tie')