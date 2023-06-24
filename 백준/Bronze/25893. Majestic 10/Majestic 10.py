n = int(input())
for n_ in range(n):
  t = list(map(int, input().split()))
  cnt, r = 0, str()
  for i in t:
    if i>=10:
      cnt += 1
  if cnt==0:
    r = 'zilch'
  elif cnt==1:
    r = 'double'
  elif cnt==2:
    r = 'double-double'
  else:
    r = 'triple-double'
  print(*t)
  print(r)
  if n_!=(n-1):
    print()