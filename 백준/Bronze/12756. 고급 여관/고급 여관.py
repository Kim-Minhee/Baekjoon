a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

while 1:
  a2 -= b1
  b2 -= a1
  if a2<=0 and b2>0:
    print('PLAYER B')
    break
  elif b2<=0 and a2>0:
    print('PLAYER A')
    break
  elif a2<=0 and b2<=0:
    print('DRAW')
    break