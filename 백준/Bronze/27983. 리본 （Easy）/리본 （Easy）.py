N = int(input())
X = list(map(int, input().split()))
L = list(map(int, input().split()))
C = list(input().split())
chk = False
for i in range(N):
  for j in range(i, N):
    if abs(X[i]-X[j])<=L[i]+L[j] and C[i]!=C[j]:
      chk = True
      print('YES')
      print(i+1, j+1)
      break
  if chk:
    break
if not chk:
  print('NO')