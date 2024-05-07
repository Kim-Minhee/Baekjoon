G1, chk = list(), False
n = 10
for i in range(n):
  g1 = list(input().split())
  G1.append(g1)

for i in range(n):
  a = G1[i][0]
  if G1[i].count(a)==n:
    chk = True
    break

if not chk:
  G2 = list()
  for _ in range(n):
    G2.append([])
  for i in range(n):
    for j in range(n):
      G2[j].append(G1[i][j])
  
  for k in range(n):
    b = G2[k][0]
    if G2[k].count(b)==n:
      chk = True
      break

if chk:
  print(1)
else:
  print(0)