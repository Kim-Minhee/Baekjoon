N = int(input())
F = list(map(int, input().split()))

chk = False
for i in range(N-2):
  if F[i]!=F[i+1] and F[i+1]!=F[i+2] and F[i]!=F[i+2]:
    chk = True
    break

if chk:
  print('TAK')
else:
  print('NIE')