A, B = map(int, input().split())
i = 1
while 1:
  if i%2!=0:
    B += A
  else:
    A += B
  if A>=5:
    print('yj')
    break
  elif B>=5:
    print('yt')
    break
  i += 1