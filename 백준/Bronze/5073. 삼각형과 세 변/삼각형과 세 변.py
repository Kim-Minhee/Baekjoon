while 1:
  a = list(map(int, input().split()))
  if a==[0, 0, 0]:
    break
  a.sort()
  if a[0]+a[1]<=a[2]:
    print('Invalid')
  elif a[0]==a[1]==a[2]:
    print('Equilateral')
  elif a[0]!=a[1] and a[1]!=a[2]:
    print('Scalene')
  else:
    print('Isosceles')