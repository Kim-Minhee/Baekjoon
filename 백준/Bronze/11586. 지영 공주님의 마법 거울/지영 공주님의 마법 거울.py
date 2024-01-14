n, p = int(input()), list()
for _ in range(n):
  p.append(list(input()))

k, p2 = int(input()), list()
if k==2:
  for i in range(n):
    p2.append(list(reversed(p[i])))
elif k==3:
  for i in range(-1, -n-1, -1):
    p2.append(p[i])
else:
  p2 = p

for i in range(n):
  print(''.join(p2[i]))