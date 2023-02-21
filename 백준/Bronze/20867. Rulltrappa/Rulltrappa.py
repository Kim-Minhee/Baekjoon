m, s, g = map(int, input().split())
a, b = map(float, input().split())
l, r = map(int, input().split())

left = (m/g)+(1/a)*l
right = (m/s)+(1/b)*r
if left<right:
  print('friskus')
else:
  print('latmask')