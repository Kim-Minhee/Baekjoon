name, fbi = list(), list()
for _ in range(5):
  name.append(input())
for n in name:
  if 'FBI' in n:
    fbi.append(name.index(n)+1)
if len(fbi)==0:
  print('HE GOT AWAY!')
else:
  print(*fbi)