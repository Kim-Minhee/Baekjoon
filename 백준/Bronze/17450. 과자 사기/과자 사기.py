m, s = -1, -1
for i in range(3):
  p, w = map(int, input().split())
  if p>=500:
    a = (10*w)/(10*p-500)
  else:
    a = (10*w)/(10*p)
  if a>m:
    m = a
    s = i
if s==0:
  print('S')
elif s==1:
  print('N')
else:
  print('U')