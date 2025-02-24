N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 10000
chk = True
r = []
for i in range(N):
  if A[i]==B[i]:
    r.append(0)
    continue
  
  if P==Q:
    chk = False
    break

  x = (B[i]-A[i])/(P-Q)
  if x>0 and x.is_integer() and cnt>=x:
    r.append(int(x))
    cnt -= x
  else:
    chk = False
    break

if chk:
  print('YES')
  print(*r)
else:
  print('NO')