N, L, D = map(int, input().split())
song, ring, chk = L*N+5*(N-1), list(), 0
for r in range(0, song+1, D):
  ring.append(r)
for i in range(1, N+1):
  for r in ring:
    if L*i+5*(i-1)<=r and r<(L+5)*i:
      print(r)
      chk = 1
      break
  if chk:
    break
if not chk:
  print(ring[-1]+D)