n = int(input())
for j in range(n):
  d = list(map(int, input().split()))
  del d[0]
  r = 'Good coin denominations!'
  for i in range(len(d)-1):
    if d[i+1]<(d[i]*2):
      r = 'Bad coin denominations!'
      break
  print('Denominations:', *d)
  print(r)
  if j!=(n-1):
    print()