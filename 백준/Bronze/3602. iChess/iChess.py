B, W = map(int, input().split())
if B<1 and W<1:
  print('Impossible')
else:
  a = max(B, W)
  b = min(B, W)
  if a!=b and a-b>1: a = b+1

  r = int((a+b)**(1/2))
  print(r)