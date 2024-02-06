n, k = map(int, input().split())
alst = list(map(int, input().split()))
hab = 0
for a in alst:
  if a%2==0:
    hab += a//2
  else:
    hab += (a//2+1)
if hab>=n:
    print('YES')
else:
  print('NO')