s = input()
mobis = ['M', 'O', 'B', 'I', 'S']
for w in mobis:
  if w not in s:
    print('NO')
    break
  else:
    if w=='S':
      print('YES')