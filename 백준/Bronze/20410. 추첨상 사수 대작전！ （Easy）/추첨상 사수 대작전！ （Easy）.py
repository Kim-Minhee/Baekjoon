M, S, X1, X2 = map(int, input().split())
b = False
for a in range(M):
  for c in range(M):
    if X1==(a*S+c)%M and X2==(a*X1+c)%M:
      print(a, c)
      b = True
      break
  if b:
    break