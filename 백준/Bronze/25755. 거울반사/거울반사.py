W, N = input().split()

r = []
for _ in range(int(N)):
  L = list(map(int, input().split()))
  for i in range(int(N)):
    if L[i]==2: L[i] = 5
    elif L[i]==5: L[i] = 2
    elif L[i] not in [1, 8]: L[i] = '?'
  if W in ['L', 'R']:
    r.append(L[::-1])
  else:
    r.append(L)

if W in ['U', 'D']:
  r = r[::-1]

for i in range(int(N)):
  print(*r[i])