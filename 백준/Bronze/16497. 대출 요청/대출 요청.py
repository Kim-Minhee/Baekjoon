date_bo, date_re = [], []
for _ in range(int(input())):
  B, R = map(int, input().split())
  date_bo.append(B)
  date_re.append(R)
K = int(input())

date_bo.sort()
date_re.sort()

chk = True
for i in range(1, 32):
  K += date_re.count(i)
  K -= date_bo.count(i)
  if K<0: chk = False; break

if chk: print(1)
else: print(0)