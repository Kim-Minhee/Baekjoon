for _ in range(3):
  y = list(map(int, input().split()))
  r = sum(y)
  if r==3:
    print('A')
  elif r==2:
    print('B')
  elif r==1:
    print('C')
  elif r==0:
    print('D')
  else:
    print('E')